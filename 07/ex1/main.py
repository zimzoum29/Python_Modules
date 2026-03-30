from ex0 import CreatureCard
from ex0 import CardRarity, SpellEffect
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from .Deck import Deck


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")

    deck = Deck()

    dragon = CreatureCard("Fire Dragon", 5, CardRarity.LEGENDARY, 7, 5)
    bolt = SpellCard(
        "Lightning Bolt", 3, CardRarity.COMMON, SpellEffect.DAMAGE)
    crystal = ArtifactCard("Mana Crystal", 2, CardRarity.RARE, 3, "+1 mana")

    print("Building deck with different card types...")
    deck.add_card(dragon)
    deck.add_card(crystal)
    deck.add_card(bolt)

    print(f"Deck stats: {deck.get_deck_stats()}\n")

    print("Drawing and playing cards:\n")
    for _ in range(3):
        card = deck.draw_card()
        if card:
            card_type = card.__class__.__name__.rstrip("Card")
            print(f"Drew: {card.name} ({card_type})")
            print(f"Play result: {card.play({})}")
        print()

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
