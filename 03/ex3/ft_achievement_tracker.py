def main() -> None:
    print("=== Achievement Tracker System ===\n")

    rayan = set([
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon"
    ])
    pablo = set([
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector"
    ])
    matisse = set([
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    ])

    print(f"Player Rayan achievements: {rayan}")
    print(f"Player Pablo achievements: {pablo}")
    print(f"Player Matisse achievements: {matisse}\n")

    print("=== Achievement Analytics ===")

    all_achievements = rayan.union(pablo).union(matisse)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")

    common_all = rayan.intersection(pablo).intersection(matisse)
    print(f"Common to all players: {common_all}")

    rayan_unique = rayan.difference(pablo.union(matisse))
    pablo_unique = pablo.difference(rayan.union(matisse))
    matisse_unique = matisse.difference(rayan.union(pablo))
    rare = rayan_unique.union(pablo_unique).union(matisse_unique)

    print(f"Rare achievements (1 player): {rare}\n")

    print(f"Rayan vs Pablo common: {rayan.intersection(pablo)}")
    print(f"Rayan unique: {rayan.difference(pablo)}")
    print(f"Pablo unique: {pablo.difference(rayan)}")


if __name__ == "__main__":
    main()
