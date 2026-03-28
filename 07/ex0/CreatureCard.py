from ex0.Card import Card
from typing import Dict


class CreatureCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        if attack < 0 or health < 0:
            raise ValueError("L'attaque et la santé doivent être positives.")
        self.attack = attack
        self.health = health

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target: str) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }

    def get_card_info(self) -> Dict:
        info = super().get_card_info()
        info.update({
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        })
        return info
