"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
Interactive SSH shell over WebSocket for Juniper EX/SRX devices.

This module provides:
- ``ShellSession`` — a programmatic bidirectional WebSocket session
- ``create_shell_session()`` — factory that calls the shell API and returns
  a connected ``ShellSession``
- ``interactive_shell()`` — convenience function that takes over the terminal
  for human SSH access
"""

import json
import os
import select
import ssl
import sys
import threading
import time
from typing import TYPE_CHECKING

import websocket

from mistapi.__logger import logger as LOGGER

if TYPE_CHECKING:
    from mistapi import APISession


class ShellSession:
    """
    Bidirectional WebSocket session for SSH-over-WebSocket shell access.

    Connects to the WebSocket URL returned by the Mist shell API endpoint
    and provides methods to send/receive raw terminal data.

    USAGE PATTERNS
    -----------
    Programmatic::

        session = create_shell_session(apisession, site_id, device_id)
        session.send_commands(["show version"])
        while session.connected:
            data = session.recv()
            if data:
                print(data.decode("utf-8", errors="replace"), end="")
        session.disconnect()

    Context manager::

        with create_shell_session(apisession, site_id, device_id) as session:
            session.send_commands(["show interfaces terse"])
            import time; time.sleep(5)
            while True:
                data = session.recv()
                if data is None:
                    break
                print(data.decode("utf-8", errors="replace"), end="")

    Interactive (human at the keyboard)::

        interactive_shell(apisession, site_id, device_id)
    """

    def __init__(
        self,
        mist_session: "APISession",
        ws_url: str,
        rows: int = 24,
        cols: int = 80,
    ) -> None:
        """
        PARAMS
        -----------
        mist_session : mistapi.APISession
            Authenticated API session (used for auth headers/cookies/SSL).
        ws_url : str
            WebSocket URL from createSiteDeviceShellSession response.
        rows : int
            Initial terminal row count.
        cols : int
            Initial terminal column count.
        """
        self._mist_session = mist_session
        self._ws_url = ws_url
        self._rows = rows
        self._cols = cols
        self._ws: websocket.WebSocket | None = None
        self._recv_buffer: list[bytes] = []
        self._shell_ready = False

    # ------------------------------------------------------------------
    # Auth / SSL helpers (mirrors _MistWebsocket but avoids coupling)

    def _get_headers(self) -> list[str]:
        if self._mist_session._apitoken:
            token = self._mist_session._apitoken[self._mist_session._apitoken_index]
            return [f"Authorization: Token {token}"]
        return []

    def _get_cookie(self) -> str | None:
        cookies = self._mist_session._session.cookies
        if cookies:
            safe = []
            for c in cookies:
                has_crlf = (
                    "\r" in c.name
                    or "\n" in c.name
                    or (c.value and ("\r" in c.value or "\n" in c.value))
                )
                if has_crlf:
                    LOGGER.warning(
                        "Skipping cookie %r: contains CRLF characters",
                        c.name,
                    )
                    continue
                safe.append(f"{c.name}={c.value}")
            return "; ".join(safe) if safe else None
        return None

    def _build_sslopt(self) -> dict:
        sslopt: dict = {}
        session = self._mist_session._session
        if session.verify is False:
            sslopt["cert_reqs"] = ssl.CERT_NONE
            sslopt["check_hostname"] = False
        elif isinstance(session.verify, str):
            sslopt["ca_certs"] = session.verify
        if session.cert:
            if isinstance(session.cert, str):
                sslopt["certfile"] = session.cert
            elif isinstance(session.cert, tuple):
                sslopt["certfile"] = session.cert[0]
                if len(session.cert) > 1:
                    sslopt["keyfile"] = session.cert[1]
        return sslopt

    # ------------------------------------------------------------------
    # Lifecycle

    def connect(self) -> None:
        """Open the WebSocket connection."""
        if self._ws is not None and self._ws.connected:
            raise RuntimeError("Already connected; call disconnect() first")
        LOGGER.info("Connecting to shell WebSocket: %s", self._ws_url)
        self._ws = websocket.create_connection(
            self._ws_url,
            header=self._get_headers(),
            cookie=self._get_cookie(),
            sslopt=self._build_sslopt(),
        )
        try:
            self._ws.settimeout(0.1)
            self.resize(self._rows, self._cols)
        except Exception:
            self.disconnect()
            raise
        LOGGER.info("Shell WebSocket connected")

    def disconnect(self) -> None:
        """Close the WebSocket connection."""
        ws = self._ws
        self._ws = None
        self._shell_ready = False
        self._recv_buffer.clear()
        if ws:
            try:
                ws.close()
            except Exception:
                pass

    @property
    def connected(self) -> bool:
        """True if the WebSocket is currently connected."""
        ws = self._ws
        return ws is not None and ws.connected

    # ------------------------------------------------------------------
    # I/O

    def send(self, data: bytes) -> None:
        """Send raw bytes (keystrokes) to the device shell."""
        ws = self._ws
        if ws and ws.connected:
            self._wait_for_shell_ready()
            if ws.connected:
                try:
                    ws.send_binary(data)
                except websocket.WebSocketConnectionClosedException:
                    pass

    def send_text(self, text: str) -> None:
        """Send a text string as binary data to the device shell."""
        self.send(f"\x00{text}".encode("utf-8"))

    def send_commands(self, commands: list[str]) -> None:
        """Send commands, adding a newline after each command."""
        text = "".join(command.rstrip("\n") + "\n" for command in commands)
        self.send_text(text)

    def recv(self, timeout: float = 0.1) -> bytes | None:
        """
        Receive raw bytes from the device shell.

        Returns None if no data is available within the timeout, or if
        the connection is closed.
        """
        if self._recv_buffer:
            return self._recv_buffer.pop(0)
        ws = self._ws
        if not ws or not ws.connected:
            return None
        old_timeout = ws.gettimeout()
        try:
            ws.settimeout(timeout)
            data = ws.recv()
            if isinstance(data, str):
                data = data.encode("utf-8")
            if data:
                self._shell_ready = True
            return data
        except websocket.WebSocketTimeoutException:
            return None
        except (
            websocket.WebSocketConnectionClosedException,
            ConnectionError,
        ):
            return None
        finally:
            try:
                ws.settimeout(old_timeout)
            except (
                websocket.WebSocketConnectionClosedException,
                ConnectionError,
                OSError,
            ) as exc:
                LOGGER.debug(
                    "ShellSession.recv: failed to restore websocket timeout "
                    "(socket may be closed): %s",
                    exc,
                )

    def _wait_for_shell_ready(self, timeout: float = 10.0) -> None:
        """Wait for first shell output before sending keystrokes."""
        if self._shell_ready:
            return
        ws = self._ws
        if not ws or not ws.connected:
            return

        old_timeout = ws.gettimeout()
        deadline = time.monotonic() + timeout
        try:
            while (
                time.monotonic() < deadline and ws.connected and not self._shell_ready
            ):
                ws.settimeout(min(0.25, max(0.01, deadline - time.monotonic())))
                try:
                    data = ws.recv()
                except websocket.WebSocketTimeoutException:
                    continue
                except (
                    websocket.WebSocketConnectionClosedException,
                    ConnectionError,
                ):
                    return
                if isinstance(data, str):
                    data = data.encode("utf-8")
                if data:
                    self._recv_buffer.append(data)
                    self._shell_ready = True
                    return
            self._shell_ready = True
        finally:
            try:
                ws.settimeout(old_timeout)
            except (
                websocket.WebSocketConnectionClosedException,
                ConnectionError,
                OSError,
            ) as exc:
                LOGGER.debug(
                    "ShellSession._wait_for_shell_ready: failed to restore "
                    "websocket timeout (socket may be closed): %s",
                    exc,
                )

    def resize(self, rows: int, cols: int) -> None:
        """Send a terminal resize message to the device."""
        self._rows = rows
        self._cols = cols
        ws = self._ws
        if ws and ws.connected:
            ws.send(json.dumps({"resize": {"width": cols, "height": rows}}))

    # ------------------------------------------------------------------
    # Context manager

    def __enter__(self) -> "ShellSession":
        return self

    def __exit__(self, *args) -> None:
        self.disconnect()


def create_shell_session(
    apisession: "APISession",
    site_id: str,
    device_id: str,
    rows: int = 24,
    cols: int = 80,
) -> ShellSession:
    """
    Call the shell API and return a connected ShellSession.

    PARAMS
    -----------
    apisession : mistapi.APISession
        Authenticated API session.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to connect to.
    rows : int
        Initial terminal row count.
    cols : int
        Initial terminal column count.

    RETURNS
    -----------
    ShellSession
        A connected ShellSession ready for send/recv.

    RAISES
    -----------
    RuntimeError
        If the API call fails or no WebSocket URL is returned.
    """
    from mistapi.api.v1.sites import devices

    response = devices.createSiteDeviceShellSession(
        apisession, site_id=site_id, device_id=device_id, body={}
    )
    if response.status_code != 200:
        raise RuntimeError(
            f"Shell API call failed: {response.status_code} - {response.data}"
        )
    if not isinstance(response.data, dict) or "url" not in response.data:
        raise RuntimeError(
            f"Shell API response did not contain a WebSocket URL: {response.data}"
        )

    ws_url = response.data["url"]
    session = ShellSession(apisession, ws_url, rows=rows, cols=cols)
    session.connect()
    return session


def _posix_input_loop(session: ShellSession) -> None:
    """Forward raw keystrokes from a POSIX TTY until the session closes.

    The terminal is put in raw mode, so control characters (including
    Ctrl+C) are forwarded to the device instead of being handled locally.
    """
    import termios
    import tty

    stdin_fd = sys.stdin.fileno()
    old_stdin_settings = termios.tcgetattr(stdin_fd)
    try:
        tty.setraw(stdin_fd)
        while session.connected:
            readable, _, _ = select.select([sys.stdin], [], [], 0.1)
            if not readable:
                continue
            data = os.read(stdin_fd, 1024)
            if not data:
                break
            session.send(b"\x00" + data)
    finally:
        termios.tcsetattr(stdin_fd, termios.TCSADRAIN, old_stdin_settings)


# Second half of the two-part console key codes returned by msvcrt.getwch()
# (after a "\x00"/"\xe0" prefix), mapped to the ANSI sequences the device
# pty expects.
_WINDOWS_KEY_ESCAPES = {
    "H": "\x1b[A",  # up
    "P": "\x1b[B",  # down
    "M": "\x1b[C",  # right
    "K": "\x1b[D",  # left
    "G": "\x1b[H",  # home
    "O": "\x1b[F",  # end
    "S": "\x1b[3~",  # delete
    "I": "\x1b[5~",  # page up
    "Q": "\x1b[6~",  # page down
}


def _windows_input_loop(session: ShellSession) -> None:
    """Forward keystrokes from the Windows console until the session closes.

    Unlike the POSIX raw-mode loop, Ctrl+C raises KeyboardInterrupt here
    (the console is not in raw mode), so it ends the session locally.
    """
    import ctypes
    import msvcrt

    # Legacy consoles need virtual terminal processing enabled to render
    # the ANSI sequences the device sends; Windows Terminal already has it.
    try:
        kernel32 = ctypes.windll.kernel32  # type: ignore[attr-defined]
        handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
        mode = ctypes.c_uint32()
        if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            kernel32.SetConsoleMode(handle, mode.value | 0x0004)
    except (OSError, AttributeError):
        pass

    while session.connected:
        if not msvcrt.kbhit():  # type: ignore[attr-defined]
            time.sleep(0.05)
            continue
        ch = msvcrt.getwch()  # type: ignore[attr-defined]
        if ch in ("\x00", "\xe0"):
            seq = _WINDOWS_KEY_ESCAPES.get(msvcrt.getwch())  # type: ignore[attr-defined]
            if seq is None:
                continue
            ch = seq
        session.send(b"\x00" + ch.encode("utf-8"))


def interactive_shell(
    apisession: "APISession",
    site_id: str,
    device_id: str,
) -> None:
    """
    Launch an interactive SSH shell session to a device.

    Takes over the terminal: captures keystrokes, sends them to the device,
    and displays output. Blocks until the connection closes (e.g. after
    typing ``exit`` on the device). On POSIX systems the terminal runs in
    raw mode, so Ctrl+C is forwarded to the device rather than ending the
    session; on Windows, Ctrl+C ends the session locally.

    PARAMS
    -----------
    apisession : mistapi.APISession
        Authenticated API session.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to connect to.

    RAISES
    -----------
    RuntimeError
        If stdin is not an interactive terminal (TTY). Use ShellSession
        for programmatic access.
    """
    if not sys.stdin.isatty():
        raise RuntimeError(
            "interactive_shell requires an interactive terminal (stdin is "
            "not a TTY); use ShellSession/create_shell_session for "
            "programmatic access"
        )

    try:
        cols, rows = os.get_terminal_size()
    except OSError:
        rows, cols = 24, 80

    session = create_shell_session(apisession, site_id, device_id, rows=rows, cols=cols)

    def _reader():
        """Background thread: read from WebSocket, write to stdout."""
        while session.connected:
            data = session.recv(timeout=0.1)
            if data:
                sys.stdout.buffer.write(data)
                sys.stdout.buffer.flush()

    reader_thread = threading.Thread(target=_reader, daemon=True)
    reader_thread.start()

    try:
        if os.name == "nt":
            _windows_input_loop(session)
        else:
            _posix_input_loop(session)
    except KeyboardInterrupt:
        pass
    finally:
        session.disconnect()
        reader_thread.join(timeout=2)
