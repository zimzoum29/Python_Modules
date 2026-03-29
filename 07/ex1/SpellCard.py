from ex0 import Card


class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Deal 3 {self.effect_type} to target"
        }

    def resolve_effect(self, targets: list[str]) -> dict:
        return {
            "spell": self.name,
            "type": self.effect_type,
            "targets_affected": len(targets)
        }
