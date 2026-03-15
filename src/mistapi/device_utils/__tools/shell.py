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
import ssl
import sys
import threading
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
        session.send_text("show version\\r\\n")
        while session.connected:
            data = session.recv()
            if data:
                print(data.decode("utf-8", errors="replace"), end="")
        session.disconnect()

    Context manager::

        with create_shell_session(apisession, site_id, device_id) as session:
            session.send_text("show interfaces terse\\r\\n")
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
        LOGGER.info("Connecting to shell WebSocket: %s", self._ws_url)
        self._ws = websocket.create_connection(
            self._ws_url,
            header=self._get_headers(),
            cookie=self._get_cookie(),
            sslopt=self._build_sslopt(),
        )
        self._ws.settimeout(0.1)
        self.resize(self._rows, self._cols)
        LOGGER.info("Shell WebSocket connected")

    def disconnect(self) -> None:
        """Close the WebSocket connection."""
        if self._ws:
            try:
                self._ws.close()
            except Exception:
                pass
            self._ws = None

    @property
    def connected(self) -> bool:
        """True if the WebSocket is currently connected."""
        return self._ws is not None and self._ws.connected

    # ------------------------------------------------------------------
    # I/O

    def send(self, data: bytes) -> None:
        """Send raw bytes (keystrokes) to the device shell."""
        if self._ws and self._ws.connected:
            self._ws.send_binary(data)

    def send_text(self, text: str) -> None:
        """Send a text string as binary data to the device shell."""
        data = bytearray()
        data.extend(map(ord, f"\x00{text}"))
        self.send(bytes(data))

    def recv(self, timeout: float = 0.1) -> bytes | None:
        """
        Receive raw bytes from the device shell.

        Returns None if no data is available within the timeout, or if
        the connection is closed.
        """
        if not self._ws or not self._ws.connected:
            return None
        old_timeout = self._ws.gettimeout()
        try:
            self._ws.settimeout(timeout)
            data = self._ws.recv()
            if isinstance(data, str):
                return data.encode("utf-8")
            return data
        except websocket.WebSocketTimeoutException:
            return None
        except (
            websocket.WebSocketConnectionClosedException,
            ConnectionError,
        ):
            return None
        finally:
            self._ws.settimeout(old_timeout)

    def resize(self, rows: int, cols: int) -> None:
        """Send a terminal resize message to the device."""
        self._rows = rows
        self._cols = cols
        if self._ws and self._ws.connected:
            self._ws.send(json.dumps({"resize": {"width": cols, "height": rows}}))

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


def interactive_shell(
    apisession: "APISession",
    site_id: str,
    device_id: str,
) -> None:
    """
    Launch an interactive SSH shell session to a device.

    Takes over the terminal: captures keystrokes, sends them to the device,
    and displays output. Blocks until the connection closes or the user
    presses Ctrl+C.

    PARAMS
    -----------
    apisession : mistapi.APISession
        Authenticated API session.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to connect to.
    """
    from sshkeyboard import listen_keyboard

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

    def _on_key_release(key: str) -> None:
        """Handle a key release event from sshkeyboard."""
        if not session.connected:
            return
        if key == "enter":
            k = "\r\n"
        elif key == "space":
            k = " "
        elif key == "tab":
            k = "\t"
        elif key == "up":
            k = "\x1b[A"
        elif key == "right":
            k = "\x1b[C"
        elif key == "down":
            k = "\x1b[B"
        elif key == "left":
            k = "\x1b[D"
        elif key == "backspace":
            k = "\x7f"
        else:
            k = key
        data = f"\x00{k}"
        data_bytes = bytearray()
        data_bytes.extend(map(ord, data))
        session.send(bytes(data_bytes))

    reader_thread = threading.Thread(target=_reader, daemon=True)
    reader_thread.start()

    try:
        listen_keyboard(
            on_release=_on_key_release,
            delay_second_char=0,
            delay_other_chars=0,
            lower=False,
        )
    except KeyboardInterrupt:
        pass
    finally:
        session.disconnect()
        reader_thread.join(timeout=2)
