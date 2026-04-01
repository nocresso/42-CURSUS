from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from typing import Dict, Any


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack_power: int, defense: int,
                 card_id: str):
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.card_id = card_id
        self.wins = 0
        self.losses = 0
        self.rating = 1200

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16 * losses

    def get_rank_info(self) -> Dict[str, Any]:
        return {
            "id": self.card_id,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def play(self, game_state: dict) -> Dict[str, Any]:
        available_mana = game_state["available_mana"]
        if self.is_playable(available_mana):
            print("Playable: True")
        else:
            print("Playable: False")
        return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Super fire ball!"
            }

    def get_tournament_stats(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "rank_info": self.get_rank_info()
        }

    def attack(self, target: str) -> Dict[str, Any]:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        return {
            "attack": self.attack_power
        }
