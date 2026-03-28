from ex3.GameStrategy import GameStrategy
from typing import Dict, List


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        played = [c.name for c in hand if c.cost <= 3]
        return {
            "cards_played": played,
            "mana_used": sum(c.cost for c in hand if c.cost <= 3),
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": 8
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        return ["Enemy Player"] + available_targets
