from ex3.GameStrategy import GameStrategy
from typing import Dict, Any, List


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AgressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> List[Any]:
        return ["Enemy Player"]

    def execute_turn(self, hand: list, battlefield: list) -> Dict[str, Any]:
        if hand:
            card = hand[0]
            return {
                "strategy": self.get_strategy_name(),
                "actions": {
                    "cards_played": card.name,
                    "mana_used": card.cost,
                    "targets_attacked": self.prioritize_targets(battlefield),
                    "damage_dealt": 8
                }
            }
        else:
            return {
                "Strategy": self.get_strategy_name(),
                "Actions": "No actions"
            }
