def main() -> None:
    print("=== Circular Curse Breaking ===")
    print()
    print("Testing ingredient validation:")
    from alchemy.grimoire.validator import validate_ingredients
    print("validate_ingredients(\"fire air\"):"
          f" {validate_ingredients('fire air')}")
    print("validate_ingredients(\"dragon scales\"):"
          f" {validate_ingredients('dragon scales')}")
    print()
    print("Testing spell recording with validation:")
    from alchemy.grimoire.spellbook import record_spell
    print("record_spell(\"Fireball\", \"fire air\"):"
          f" {record_spell('Fireball', 'fire air')}")
    print("record_spell(\"Dark Magic\", \"shadow\"):"
          f" {record_spell('Dark Magic', 'shadow')}")
    print()
    print("Testing deferred import technique:")
    print("record_spell(\"Lightning\", \"air\"):"
          f" {record_spell('Lightning', 'air')}")
    print("record_spell(\"Super Bowl\", \"moon\"):"
          f" {record_spell('Super Bowl', 'moon')}")
    print()
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
