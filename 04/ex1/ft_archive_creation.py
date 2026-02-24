def main() -> None:
    filename: str = "new_discovery.txt"
    entries: list[str] = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee",
    ]

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print(f"Initializing new storage unit: {filename}")

    f = open(filename, "w", encoding="utf-8")
    try:
        print("Storage unit created successfully...")
        print("Inscribing preservation data...")
        for line in entries:
            f.write(line + "\n")
            print(line)
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")
    finally:
        f.close()


if __name__ == "__main__":
    main()
