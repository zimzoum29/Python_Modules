from abc import ABC, abstractmethod


class Identifiable(ABC):

    @abstractmethod
    def get_unique_id(self) -> str:
        pass

    @abstractmethod
    def get_owner_name(self) -> str:
        pass
