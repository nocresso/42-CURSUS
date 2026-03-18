from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Dict, Any


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int,
                 rarity: str, combat_type: str, attack_power: int, mana: int):
        super().__init__(name, cost, rarity)
        self.combat_type = combat_type
        self.attack_power = attack_power
        self.mana = mana

    def attack(self, target: str) -> Dict[str, Any]:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": 3,
            "still_alive": True
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        return {
            "attack": self.attack_power,
            "combat_type": self.combat_type
        }

    def cast_spell(self, spell_name: str, targets: list) -> Dict[str, Any]:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": 4
        }

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        return {
            "channeled": amount,
            "total_mana": amount + self.mana
        }

    def get_magic_stats(self) -> Dict[str, Any]:
        return {
            "final_mana": self.mana
        }

    def get_card_info(self) -> Dict[str, Any]:
        card_info = super().get_card_info()
        try:
            card_info["type"] = "Elite Card"
            card_info["combat_type"] = self.combat_type
            card_info["attack"] = self.attack_power
            card_info["mana"] = self.mana
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
                "effect": "Super Elite creature appeared!"
            }
