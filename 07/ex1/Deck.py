import random
from ex0 import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class Deck:

    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            print("The deck is empty.")
            return None
        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        avg = sum(c.cost for c in self.cards) / (len(self.cards) or 1)
        return {
            "total_cards": len(self.cards),
            "creatures": sum(1 for card in self.cards if isinstance(
                card, CreatureCard)),
            "spells": sum(1 for card in self.cards if isinstance(
                card, SpellCard)),
            "artifacts": sum(1 for card in self.cards if isinstance(
                card, ArtifactCard)),
            "avg_cost": avg
        }
