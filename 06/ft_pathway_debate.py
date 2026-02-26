import alchemy.transmutation


def main():
    print("=== Pathway Debate Mastery ===")

    print("\nAbsolute imports (basic.py):")
    print("lead_to_gold():", alchemy.transmutation.lead_to_gold())
    print("stone_to_gem():", alchemy.transmutation.stone_to_gem())

    print("\nRelative imports (advanced.py):")
    print("philosophers_stone():", alchemy.transmutation.philosophers_stone())
    print("elixir_of_life():", alchemy.transmutation.elixir_of_life())

    print("\nBoth pathways work!")


if __name__ == "__main__":
    main()