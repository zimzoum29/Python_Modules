from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:

    def __init__(self):
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.hand = []
        self.battlefield = []
        self.turns = 0
        self.total_damage = 0

    def configure_engine(
            self,
            factory: CardFactory, strategy: GameStrategy
                ) -> None:
        self.factory = factory
        self.strategy = strategy

        deck_data = self.factory.create_themed_deck(3)
        self.hand = deck_data["deck"]

    def simulate_turn(self) -> dict:
        if not self.strategy:
            raise ValueError("Strategy not configured")

        result = self.strategy.execute_turn(self.hand, self.battlefield)

        self.turns += 1
        self.total_damage += result["damage_dealt"]

        return result

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": len(self.hand)
        }
