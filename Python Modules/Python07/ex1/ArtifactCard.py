from ex0.Card import Card
from typing import Dict, Any


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict) -> Dict[str, str]:
        available_mana = game_state["available_mana"]
        if self.is_playable(available_mana):
            print("Playable: True")
        else:
            print("Playable: False")
        return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect
            }

    def get_card_info(self) -> Dict[str, str]:
        card_info = super().get_card_info()
        try:
            card_info["type"] = "Artifact"
            card_info["durability"] = self.durability
            card_info["effect"] = self.effect
            return card_info
        except ValueError as e:
            print(f"{e}")
            return

    def activate_ability(self) -> Dict[str, Any]:
        return {
            "card_played": self.name,
            "ability": "activated"
        }
