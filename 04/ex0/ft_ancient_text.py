def main() -> None:
    filename: str = "ancient_fragment.txt"

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {filename}")

    try:
        f = open(filename, "r", encoding="utf-8")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return

    try:
        print("Connection established...\n")
        print("RECOVERED DATA:")
        for line in f:
            print(line.rstrip("\n"))
        print("\nData recovery complete. Storage unit disconnected.")
    finally:
        f.close()


if __name__ == "__main__":
    main()
