def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    print("SECURE EXTRACTION:")
    with open("classified_vault.txt", "r") as f:
        for line in f:
            print(line.rstrip("\n"))

    print("SECURE PRESERVATION:")
    with open("security_protocols.txt", "w") as f:
        f.write("[CLASSIFIED] New security protocols archived\n")

    print("[CLASSIFIED] New security protocols archived")
    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
