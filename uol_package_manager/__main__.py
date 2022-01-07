import os
import sys
import string

from uol_package_manager.utils import is_installed, get_system_package_managers, has_sudo

from uol_package_manager.settings import PACKAGE_MANAGERS_INSTALL

called_package_manager = sys.argv[1]
called_args = " ".join(sys.argv[2:])
if has_sudo():
    sudo = "sudo "
else:
    sudo = ""

if is_installed(called_package_manager):
    print(f'your system has {called_package_manager} installed')
else:
    installed_managers = get_system_package_managers()
    installed_managers_text = ", ".join(installed_managers)
    print(f'you system does not have {installed_managers_text} installed')
    print('you can try to install the pack with the package name might not be the same')
    for installed in installed_managers:
        if installed not in PACKAGE_MANAGERS_INSTALL:
            continue
        message = PACKAGE_MANAGERS_INSTALL[installed].replace("{package_name}", called_args).replace("{package_manager_name}", installed)
        print(f'{sudo}{message}')