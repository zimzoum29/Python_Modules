from .EliteCard import EliteCard
from .Combatable import Combatable
from .Magical import Magical
from ex0.Card import Card


def get_public_methods(cls) -> list[str]:
    return [
        meth
        for meth in dir(cls)
        if callable(getattr(cls, meth)) and not meth.startswith("__")
    ]


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")

    warrior = EliteCard("Arcane Warrior", 6, "Epic", 5, 8)

    print(EliteCard.__qualname__, "capabilities:")
    classes_to_check = [Card, Combatable, Magical]

    for cls in classes_to_check:
        methods: list[str] = get_public_methods(cls)
        print(f"- {cls.__name__}: {methods}")

    print(f"\nPlaying {warrior.name} (Elite Card):")
    warrior.play({})

    print("\nCombat phase:")
    print(f"Attack result: {warrior.attack('Enemy')}")
    print(f"Defense result: {warrior.defend(5)}")

    print("\nMagic phase:")
    print(
        "Spell cast: "
        f"{warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}"
        )
    print(f"Mana channel: {warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
