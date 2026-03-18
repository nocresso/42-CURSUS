from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("=== DataDeck Deck Builder ===")
    print()
    print("Building deck with different card types...")
    card1 = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    card2 = SpellCard("Lightning Bolt", 2, "Common", "damage")
    card3 = ArtifactCard("Mana Crystal", 2, "Common", 5,
                         "Permanent: +1 mana per turn")
    deck = Deck()
    deck.add_card(card1)
    deck.add_card(card2)
    deck.add_card(card3)
    game_status = {
        "available_mana": 15
    }
    print(f"Print stats: {deck.get_deck_stats()}")
    print()
    print("Drawing and playing cards:")
    while deck.cards:
        try:
            card = deck.draw_card()
            info = card.get_card_info()
            print(f"\nDrew: {card.name} ({info['type']})")
            print(f"Play result: {card.play(game_status)}")

        except Exception as e:
            print(f"Error: {e}")
    print()
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
