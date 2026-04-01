from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===")
    print()
    print("EliteCard capabilities:")
    print(f"- Card {['play', 'get_card_info', 'is_playable']}")
    print(f"- Combatable {['attack', 'defend', 'get_combat_stats']}")
    print(f"- Magical {['cast_spell', 'channel_mana', 'get_magic_stats']}")
    print()
    card = EliteCard("Arcane Warrior", 2, "special", "melee", 5, 3)
    info = card.get_card_info()
    print(f"Playing {card.name} ({info['type']}):")
    print()
    print("Combat phase:")
    attack_info = card.attack("Enemy")
    defend_info = card.defend(2)
    print(f"Attack results: {attack_info}")
    print(f"Defense results: {defend_info}")
    print()
    print("Magic phase:")
    spell_info = card.cast_spell("Fireball", ['Enemy1', 'Enemy2'])
    mana_info = card.channel_mana(5)
    print(f"Spell cast: {spell_info}")
    print(f"Mana channel: {mana_info}")
    print()
    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
