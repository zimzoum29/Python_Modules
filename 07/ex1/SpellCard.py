from ex0.Card import Card
from typing import Dict


class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Cast {self.effect_type} spell"
        }

    def resolve_effect(self, targets: list) -> Dict:
        return {
            "spell": self.name,
            "type": self.effect_type,
            "targets_affected": len(targets)
        }
