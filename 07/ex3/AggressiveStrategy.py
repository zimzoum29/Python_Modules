from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        played_cards = []
        mana_used = 0
        damage = 0

        for card in hand:
            if card.cost <= 3:
                played_cards.append(card.name)
                mana_used += card.cost
                damage += 3

        return {
            "cards_played": played_cards,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets
