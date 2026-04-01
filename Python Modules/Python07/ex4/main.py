from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main() -> None:
    print("=== DataDeck Tournament Platform ===")
    print()
    print("Registering Tournament Cards...")
    print()
    platform = TournamentPlatform()
    card1 = TournamentCard("Fire Dragon", 5, "common", 5, 5, "dragon_001")
    card2 = TournamentCard("Ice Wizard", 2, "legendary", 3, 3, "wizard_001")
    interfaces = [base.__name__ for base in TournamentCard.__bases__]
    platform.register_card(card1)
    platform.register_card(card2)
    print(f"{card1.name} (ID: {card1.card_id}):")
    print(f"- Interfaces: {interfaces}")
    print(f"- Rating: {card1.rating}")
    print(f"- Record: {card1.wins}-{card1.losses}")
    print()
    print(f"{card2.name} (ID: {card2.card_id}):")
    print(f"- Interfaces: {interfaces}")
    print(f"- Rating: {card2.rating}")
    print(f"- Record: {card2.wins}-{card2.losses}")
    print()
    print("Creating tournament match...")
    results = platform.create_match(card1.card_id, card2.card_id)
    print(f"Match result: {results}")
    print()
    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, player_result in enumerate(leaderboard, 1):
        print(f"{i}. {player_result}")
    print()
    print("Platform Report:")
    report = platform.generate_tournament_report()
    print(f"{report}")
    print()
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
