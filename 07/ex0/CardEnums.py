from enum import Enum


class CardRarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"

    def __str__(self) -> str:
        return self.value


class SpellEffect(Enum):
    DAMAGE = "damage"
    HEAL = "heal"

    def __str__(self) -> str:
        return self.value


class CardType(Enum):
    CREATURE = "creature"
    SPELL = "spell"
    ARTIFACT = "artifact"

    def __str__(self) -> str:
        return self.value
