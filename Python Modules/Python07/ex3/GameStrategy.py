from abc import ABC, abstractmethod
from typing import Dict, Any, List


class GameStrategy(ABC):

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> List[Any]:
        pass
