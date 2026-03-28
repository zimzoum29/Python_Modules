from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Dict, List


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack_val: int, magic_power: int):
        super().__init__(name, cost, rarity)
        self.attack_val = attack_val
        self.magic_power = magic_power
        self.mana_pool = 0

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite champion enters the field"
        }

    def attack(self, target: str) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_val,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> Dict:
        blocked = min(incoming_damage, self.attack_val // 2)
        taken = incoming_damage - blocked
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": True
        }

    def get_combat_stats(self) -> Dict:
        return {"attack": self.attack_val}

    def cast_spell(self, spell_name: str, targets: List[str]) -> Dict:
        mana_cost = 4
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost
        }

    def channel_mana(self, amount: int) -> Dict:
        self.mana_pool += amount
        return {
            "channeled": amount,
            "total_mana": self.mana_pool
        }

    def get_magic_stats(self) -> Dict:
        return {"magic_power": self.magic_power, "mana_pool": self.mana_pool}
