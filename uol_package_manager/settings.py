BIN_NAME = 'uol-pm'

PACKAGE_MANAGERS = [
    "apt",
    "apt-get",
    "apk",
    "packman",
    "yum"
]

_APT_INSTALL = "{package_manager_name} install [package_name]"

PACKAGE_MANAGERS_INSTALL = {
    "apt": _APT_INSTALL,
    "apt-get": _APT_INSTALL,
    "apk": "add [package_name]",
    "packman": "pacman -Syu [package_name]",
    "yum": "yum install [package_name]"
}