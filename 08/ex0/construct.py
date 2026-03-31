#!/usr/bin/env python3

import sys
import os
import site


def is_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def get_venv_name() -> str:
    return os.path.basename(sys.prefix)


def main() -> None:
    print()

    if is_virtual_env():
        print("MATRIX STATUS: Welcome to the construct\n")

        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {get_venv_name()}")
        print(f"Environment Path: {sys.prefix}\n")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print()

        print("Package installation path:")
        print(site.getsitepackages()[0])

    else:
        print("MATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate   # On Windows\n")


if __name__ == "__main__":
    main()
