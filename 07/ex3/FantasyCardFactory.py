from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import Dict, Union


class FantasyCardFactory(CardFactory):

    def create_creature(
            self,
            name_or_power: Union[str, int, None] = None
            ) -> CreatureCard:
        name = name_or_power if isinstance(name_or_power, str)\
                                else "Goblin Warrior"
        return CreatureCard(name, 2, "Common", 2, 2)

    def create_spell(
            self,
            name_or_power: Union[str, int, None] = None
            ) -> SpellCard:
        return SpellCard("Fireball", 3, "Rare", "damage")

    def create_artifact(
            self,
            name_or_power: Union[str, int, None] = None
            ) -> ArtifactCard:
        return ArtifactCard("Mana Ring", 1, "Epic", 5, "Add 1 mana")

    def create_themed_deck(self, size: int) -> Dict:
        return {"size": size, "theme": "Fantasy", "status": "Generated"}

    def get_supported_types(self) -> Dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
