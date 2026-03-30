from .CreatureCard import CreatureCard
from .CardEnums import CardRarity


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    dragon = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity=CardRarity.LEGENDARY,
        attack=7,
        health=5
    )

    print("CreatureCard Info:")
    print(dragon.get_card_info())

    mana_available = 6
    print(f"\nPlaying Fire Dragon with {mana_available} mana available:")
    print(f"Playable: {dragon.is_playable(mana_available)}")

    game_state = {"mana": mana_available}
    print(f"Play result: {dragon.play(game_state)}")

    target = "Goblin Warrior"
    print(f"\n{dragon.name} attacks {target}:")
    print(f"Attack result: {dragon.attack_target(target)}")

    mana_low = 3
    print(f"\nTesting insufficient mana ({mana_low} available):")
    print(f"Playable: {dragon.is_playable(mana_low)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
