from typing import Any, Iterator

from tabulate import tabulate


class _Privilege:
    def __init__(self, privilege) -> None:
        self.scope: str = ""
        self.org_id: str = ""
        self.org_name: str = ""
        self.msp_id: str = ""
        self.msp_name: str = ""
        self.orggroup_ids: list[str] = []
        self.name: str = ""
        self.role: str = ""
        self.site_id: str = ""
        self.sitegroup_ids: list[str] = []
        self.views: list[str] = []
        for key, val in privilege.items():
            setattr(self, key, val)

    def __str__(self) -> str:
        fields = [
            "scope",
            "role",
            "org_id",
            "org_name",
            "msp_id",
            "msp_name",
            "orggroup_ids",
            "name",
            "role",
            "site_id",
            "sitegroup_ids",
        ]
        string = ""
        for field in fields:
            if getattr(self, field) != "":
                string += f"{field}: {getattr(self, field)} \r\n"
        return string

    def get(self, key: str, default: Any | None = None) -> Any:
        if hasattr(self, key) and getattr(self, key):
            return getattr(self, key)
        else:
            return default


class Privileges:
    def __init__(self, privileges: list[dict]) -> None:
        self.privileges: list[_Privilege] = []
        for privilege in privileges:
            self.privileges.append(_Privilege(privilege))

    def __iter__(self) -> Iterator[_Privilege]:
        """Return an iterator over the privileges."""
        if not self.privileges:
            return iter([])
        return iter(self.privileges)

    def __str__(self) -> str:
        columns_headers = [
            "scope",
            "role",
            "name",
            "site_id",
            "org_name",
            "org_id",
            "msp_name",
            "msp_id",
            "views",
        ]
        table = []
        for entry in self.privileges:
            temp = []
            for field in columns_headers:
                if hasattr(entry, field):
                    temp.append(str(getattr(entry, field)))
                else:
                    temp.append("")
            table.append(temp)
        return tabulate(table, columns_headers)

    def display(self):
        return str(self)
