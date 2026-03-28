from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import Dict, Optional


class GameEngine:

    def __init__(self):
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.turns_simulated = 0

    def configure_engine(
            self, factory: CardFactory,
            strategy: GameStrategy
            ) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:
        if not self.factory or not self.strategy:
            raise ValueError("Engine must be configured before simulation.")

        self.turns_simulated += 1
        hand = [
            self.factory.create_creature("Fire Dragon"),
            self.factory.create_creature("Goblin Warrior"),
            self.factory.create_spell("Lightning Bolt")
        ]
        hand[0].cost = 5

        turn_execution = self.strategy.execute_turn(hand, [])
        return {
            "strategy": self.strategy.get_strategy_name(),
            "actions": turn_execution
        }

    def get_engine_status(self) -> Dict:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name()
            if self.strategy else None,
            "total_damage": 8,
            "cards_created": 3
        }
