import os

from pathlib import Path
from typing import List
from uol_package_manager.settings import BIN_NAME, PACKAGE_MANAGERS

def is_installed(package_manager: bool) -> str:
    file_path = f'/bin/{package_manager}'
    path_object = Path(file_path)
    if path_object.exists():
        if path_object.is_symlink():
            if BIN_NAME in path_object.resolve():
                return False # package manager is not installed file is pointing to us

        return True
    else:
        return False

def has_sudo() -> bool:
    return is_installed('sudo')

def is_root() -> bool:
    return os.geteuid() != 0

def get_system_package_managers() -> List[str]:
    output = []
    for x in PACKAGE_MANAGERS:
        if is_installed(x):
            output.append(x)
    return output

