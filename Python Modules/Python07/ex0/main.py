from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")
    print()
    print("Testing Abstract Base Class Design:")
    print()
    player = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    game_status = {
        "available_mana": 6
    }
    print("CreatureCard Info:")
    player_info = player.get_card_info()
    print(player_info)
    print()
    print(f"Playing {player.name} with"
          f" {game_status['available_mana']} mana available:")
    print(f"Play result: {player.play(game_status)}")
    print()
    target = "Goblin Warrior"
    print(f"{player.name} attacks {target}:")
    print(f"Attack result: {player.attack_target(target)}")
    print()
    game_stat = {
        "available_mana": 3
    }
    print(f"Testing insufficient mana"
          f" ({game_stat['available_mana']} available):")
    player.play(game_stat)
    print()
    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
