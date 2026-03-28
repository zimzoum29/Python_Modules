from abc import ABC, abstractmethod
from typing import Dict


class Rankable(ABC):

    @abstractmethod
    def update_rating(self, points: int) -> None:
        pass

    @abstractmethod
    def get_rank_info(self) -> Dict:
        pass
