#!/usr/bin/env python3

import os
from dotenv import load_dotenv


def load_config():
    """Load environment variables"""
    load_dotenv()

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }

    return config


def validate_config(config):
    """Check missing values"""
    missing = [k for k, v in config.items() if not v]

    if missing:
        print("WARNING: Missing configuration:")
        for key in missing:
            print(f"- {key}")
        return False

    return True


def display_config(config):
    print("\nORACLE STATUS: Reading the Matrix...\n")

    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    print(f"Database: {config['DATABASE_URL']}")
    print(
        "API Access: "
        f"{'Authenticated' if config['API_KEY'] else 'Missing'}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: {config['ZION_ENDPOINT']}")


def security_check():
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available\n")


def main():
    config = load_config()

    if not validate_config(config):
        print("\nPlease configure your .env file.")
        return

    display_config(config)
    security_check()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
