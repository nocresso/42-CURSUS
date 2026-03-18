from ex0.Card import Card
from typing import Dict


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def validate_info(self, attack: int, health: int) -> None:
        if attack < 0 or health < 0:
            raise ValueError("Error: Invalid value")

    def get_card_info(self) -> Dict:
        card_info = super().get_card_info()
        try:
            self.validate_info(self.attack, self.health)
            card_info["type"] = "Creature"
            card_info["attack"] = self.attack
            card_info["health"] = self.health
            return card_info
        except ValueError as e:
            print(f"{e}")
            return

    def play(self, game_state: Dict) -> Dict:
        available_mana = game_state["available_mana"]
        if self.is_playable(available_mana):
            print("Playable: True")
        else:
            print("Playable: False")
        return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            }

    def attack_target(self, target: str) -> Dict:
        return {
                "attacker": self.name,
                "target": target,
                "damage_dealt": self.attack,
                "combat_resolved": "True"
            }
