from alchemy.grimoire import record_spell, validate_ingredients


def main():
    print("=== Circular Curse Breaking ===")

    print("\nValidation:")
    print('validate_ingredients("fire air"):', validate_ingredients("fire air"))
    print('validate_ingredients("dragon scales"):', validate_ingredients("dragon scales"))

    print("\nRecording:")
    print('record_spell("Fireball", "fire air"):', record_spell("Fireball", "fire air"))
    print('record_spell("Dark Magic", "shadow"):', record_spell("Dark Magic", "shadow"))
    print('record_spell("Lightning", "air"):', record_spell("Lightning", "air"))

    print("\nCircular dependency curse avoided using late imports!")


if __name__ == "__main__":
    main()