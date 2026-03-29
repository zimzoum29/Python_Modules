import uuid
from .TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self):
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        card_id = str(uuid.uuid4())
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        if card1.attack_power >= card2.attack_power:
            winner, loser = card1, card2
            winner_id, loser_id = card1_id, card2_id
        else:
            winner, loser = card2, card1
            winner_id, loser_id = card2_id, card1_id

        winner.update_wins(1)
        loser.update_losses(1)

        self.matches_played += 1

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        leaderboard = []

        for card_id, card in self.cards.items():
            stats = card.get_tournament_stats()
            leaderboard.append((card_id, stats))

        leaderboard.sort(key=lambda x: x[1]["rating"], reverse=True)

        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)
        avg_rating = (
            sum(card.calculate_rating() for card
                in self.cards.values()) / total_cards
            if total_cards > 0 else 0
        )

        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": int(avg_rating),
            "platform_status": "active"
        }
