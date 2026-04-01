from ex4.TournamentCard import TournamentCard
from typing import Dict, Any, List


class TournamentPlatform:
    def __init__(self):
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict[str, Any]:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]
        if card1.attack_power > card2.attack_power:
            winner = card1
            loser = card2
        else:
            winner = card2
            loser = card1
        winner.update_wins(1)
        loser.update_losses(1)
        winner.calculate_rating()
        loser.calculate_rating()
        self.matches_played += 1
        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> List[str]:
        ranking = sorted(self.cards.values(),
                         key=TournamentCard.calculate_rating, reverse=True)
        return [f"{c.name} - Rating: {c.rating} ({c.wins}-{c.losses})"
                for c in ranking]

    def generate_tournament_report(self) -> Dict[str, Any]:
        if not self.cards:
            avg_rating = 0
        else:
            ratings = [c.rating for c in self.cards.values()]
            avg_rating = sum(ratings) / len(ratings)
        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
