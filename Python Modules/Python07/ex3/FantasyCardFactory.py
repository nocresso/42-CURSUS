from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import Dict, Any
from ex1.Deck import Deck
from ex0.Card import Card


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            card = CreatureCard(name_or_power, 5, "Legendary", 7, 5)
        elif isinstance(name_or_power, int):
            card = CreatureCard("Fire Dragon", name_or_power,
                                "Legendary", 7, 5)
        else:
            card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        return card

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            card = SpellCard(name_or_power, 2, "Common", "damage")
        elif isinstance(name_or_power, int):
            card = SpellCard("Lightning Bolt", name_or_power,
                             "Common", "damage")
        else:
            card = SpellCard("Lightning Bolt", 2, "Common", "damage")
        return card

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            card = ArtifactCard(name_or_power, 2, "Common", 5,
                                "Permanent: +1 mana per turn")
        elif isinstance(name_or_power, int):
            card = ArtifactCard("Mana Crystal", name_or_power, "Common", 5,
                                "Permanent: +1 mana per turn")
        else:
            card = ArtifactCard("Mana Crystal", 2, "Common", 5,
                                "Permanent: +1 mana per turn")
        return card

    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        deck = Deck()
        for i in range(size):
            if i % 3 == 0:
                card = self.create_creature()
            elif i % 3 == 1:
                card = self.create_spell()
            else:
                card = self.create_artifact()
            deck.add_card(card)
        return {
                "deck_size": size,
                "theme": "Fantasy",
                "deck": deck
                }

    def get_supported_types(self) -> Dict[str, Any]:
        return {
                "creatures": ["dragon", "goblin"],
                "spells": ["fireball"],
                "artifacts": ["mana_ring"]
                }
