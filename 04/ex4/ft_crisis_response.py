def handle_access(filename: str, label: str) -> None:
    if label == "CRISIS":
        print(f"\nCRISIS ALERT: Attempting access to '{filename}'...")
    else:
        print(f"\nROUTINE ACCESS: Attempting access to '{filename}'...")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            content: str = f.read().strip()

        if content:
            print(f"SUCCESS: Archive recovered - ``{content}''")
        else:
            print("SUCCESS: Archive recovered - ``(empty archive)''")
        print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system stable")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    handle_access("lost_archive.txt", "CRISIS")
    handle_access("classified_vault.txt", "CRISIS")
    handle_access("standard_archive.txt", "ROUTINE")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
