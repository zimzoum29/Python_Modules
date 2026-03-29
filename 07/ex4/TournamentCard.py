from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int, rarity: str, attack: int):
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.wins = 0
        self.losses = 0
        self.rating = 1200

    def play(self, game_state: dict) -> dict:
        return {"card_played": self.name}

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power
        }

    def defend(self, incoming_damage: int) -> dict:
        return {
            "damage_taken": incoming_damage
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power
        }

    def calculate_rating(self) -> int:
        return self.rating + (self.wins * 10) - (self.losses * 5)

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.calculate_rating()
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "rating": self.calculate_rating(),
            "record": f"{self.wins}-{self.losses}"
        }
