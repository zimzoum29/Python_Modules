from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("=== DataDeck Deck Builder ===")
    deck = Deck()

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    bolt = SpellCard("Lightning Bolt", 3, "Common", "damage")
    crystal = ArtifactCard("Mana Crystal", 2, "Rare", 3, "+1 mana")

    deck.add_card(dragon)
    deck.add_card(bolt)
    deck.add_card(crystal)

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")
    for _ in range(3):
        card = deck.draw_card()
        if card:
            print(f"Drew: {card.name}")
            print(f"Play result: {card.play({})}")


if __name__ == "__main__":
    main()
