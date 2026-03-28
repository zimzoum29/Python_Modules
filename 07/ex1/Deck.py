import random
from typing import List, Dict
from ex0.Card import Card


class Deck:

    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self.cards.append(card)

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise IndexError("Le deck est vide.")
        return self.cards.pop()

    def get_deck_stats(self) -> Dict:
        total = len(self.cards)
        if total == 0:
            return {"total_cards": 0}

        avg_cost = sum(c.cost for c in self.cards) / total
        return {
            "total_cards": total,
            "avg_cost": round(avg_cost, 2)
        }
