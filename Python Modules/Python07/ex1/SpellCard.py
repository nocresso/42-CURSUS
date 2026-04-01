from ex0.Card import Card
from typing import Dict, List, Any


class SpellCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: Dict) -> Dict[str, Any]:
        available_mana = game_state["available_mana"]
        if self.is_playable(available_mana):
            print("Playable: True")
        else:
            print("Playable: False")
        return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": f"Deal 3 {self.effect_type} to target"
            }

    def get_card_info(self) -> Dict[str, Any]:
        card_info = super().get_card_info()
        try:
            card_info["type"] = "Spell"
            card_info["effect_type"] = self.effect_type
            return card_info
        except ValueError as e:
            print(f"{e}")
            return

    def resolve_effect(self, targets: List) -> Dict[str, Any]:
        return {
            "card_played": self.name,
            "target": targets,
            "effect": f"Deal 3 {self.effect_type} to target"
        }
