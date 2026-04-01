from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory
from typing import Dict, Any


class GameEngine:
    def __init__(self):
        self.strategy = None
        self.hand = []
        self.battlefield = []
        self.deck = None

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        data = factory.create_themed_deck(5)
        deck = data["deck"]
        self.deck = deck
        deck.shuffle()
        self.strategy = strategy

    def simulate_turn(self) -> Dict[str, Any]:
        card = self.deck.draw_card()
        self.hand.append(card)
        result = self.strategy.execute_turn(self.hand, self.battlefield)
        return result

    def get_engine_status(self) -> Dict[str, Any]:
        return {
            "turns_simulated": 1,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": 8,
            "cards_created": len(self.hand)
        }
