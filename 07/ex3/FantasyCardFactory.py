import random
from .CardFactory import CardFactory
from ex0 import CreatureCard
from ex1 import SpellCard
from ex1 import ArtifactCard


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power=None):
        creatures = [
            ("Fire Dragon", 5, 7, 5),
            ("Goblin Warrior", 2, 3, 2)
        ]
        name, cost, attack, health = random.choice(creatures)
        return CreatureCard(name, cost, "Common", attack, health)

    def create_spell(self, name_or_power=None):
        spells = [
            ("Lightning Bolt", 3, "damage"),
            ("Healing Light", 2, "heal")
        ]
        name, cost, effect = random.choice(spells)
        return SpellCard(name, cost, "Rare", effect)

    def create_artifact(self, name_or_power=None):
        artifacts = [
            ("Mana Crystal", 2, 3, "+1 mana per turn"),
            ("Ancient Ring", 4, 5, "+2 attack")
        ]
        name, cost, durability, effect = random.choice(artifacts)
        return ArtifactCard(name, cost, "Epic", durability, effect)

    def create_themed_deck(self, size: int) -> dict:
        deck = []

        for _ in range(size):
            choice = random.choice(["creature", "spell", "artifact"])
            if choice == "creature":
                deck.append(self.create_creature())
            elif choice == "spell":
                deck.append(self.create_spell())
            else:
                deck.append(self.create_artifact())

        return {"deck": deck}

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
