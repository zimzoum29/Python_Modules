from typing import List, Dict
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self):
        self.participants: List[TournamentCard] = []
        self.match_history: List[Dict] = []

    def register_card(self, card: TournamentCard) -> None:
        if isinstance(card, TournamentCard):
            self.participants.append(card)

    def run_match(
        self,
        card_a: TournamentCard,
        card_b: TournamentCard
            ) -> Dict:
        power_a = card_a.attack_val + card_a.magic_power
        power_b = card_b.attack_val + card_b.magic_power

        winner, loser = (card_a, card_b) if power_a >= power_b \
            else (card_b, card_a)

        winner.update_rating(20)
        loser.update_rating(-15)

        result = {
            "winner": winner.get_unique_id(),
            "loser": loser.get_unique_id(),
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }
        self.match_history.append(result)
        return result

    def get_leaderboard(self) -> List[str]:
        sorted_cards = sorted(
            self.participants,
            key=lambda x: x.rating,
            reverse=True
        )
        return [
            f"{c.name} - Rating: {c.rating} ({c.wins}-{c.losses})"
            for c in sorted_cards
        ]

    def get_platform_report(self) -> Dict:
        total_rating = sum(c.rating for c in self.participants)
        return {
            "total_cards": len(self.participants),
            "matches_played": len(self.match_history),
            "avg_rating": total_rating // len(self.participants)
            if self.participants else 0
        }
