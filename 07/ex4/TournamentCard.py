from ex2.EliteCard import EliteCard
from ex4.Identifiable import Identifiable
from ex4.Rankable import Rankable
from typing import Dict


class TournamentCard(EliteCard, Identifiable, Rankable):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, magic: int, card_id: str):
        super().__init__(name, cost, rarity, attack, magic)
        self.card_id = card_id
        self.rating = 1000
        self.wins = 0
        self.losses = 0

    def get_unique_id(self) -> str:
        return self.card_id

    def get_owner_name(self) -> str:
        return "Tournament System"

    def update_rating(self, points: int) -> None:
        self.rating += points
        if points > 0:
            self.wins += 1
        else:
            self.losses += 1

    def get_rank_info(self) -> Dict:
        return {
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }
