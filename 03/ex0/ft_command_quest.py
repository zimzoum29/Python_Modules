import sys


def main():
    print("=== Command Quest ===")

    argc = len(sys.argv)
    program_name = sys.argv[0]

    if argc == 1:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {argc}")
        return

    args_received = argc - 1
    print(f"Program name: {program_name}")
    print(f"Arguments received: {args_received}")

    i = 1
    while i < argc:
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1

    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()
