#!/usr/bin/env python3

import sys
import os
import site


def is_virtual_env() -> bool:
    """Detect if running inside a virtual environment"""
    return (
        hasattr(sys, 'base_prefix') and sys.prefix != sys.base_prefix
    ) or hasattr(sys, 'real_prefix')


def get_venv_name() -> str:
    """Get virtual environment name"""
    return os.path.basename(sys.prefix)


def main() -> None:
    print("\n=== MATRIX INTERFACE ===\n")

    python_path = sys.executable
    in_venv = is_virtual_env()

    if not in_venv:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {python_path}")
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate   # On Windows\n")

    else:
        venv_name = get_venv_name()

        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {python_path}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}\n")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting global system.\n")

        print("Package installation path:")
        for path in site.getsitepackages():
            print(path)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
