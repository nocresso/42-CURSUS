from typing import Dict, Any


def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    power = initial_power

    def add_power(given_power: int) -> int:
        nonlocal power
        power = power + given_power
        return power
    return add_power


def enchantment_factory(enchantment_type: str) -> callable:
    def factory(item_name: str):
        return enchantment_type + " " + item_name
    return factory


def memory_vault() -> Dict[str, callable]:
    vault = {}

    def store(key: str, value: Any):
        vault[key] = value

    def recall(key: str):
        try:
            return vault[key]
        except KeyError:
            return "Memory not found"

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    power_additions = [8, 9, 15, 14, 9]
    enchantment_types = ['Frozen', 'Flowing', 'Windy']
    items_to_enchant = ['Sword', 'Shield', 'Amulet']
    print("Testing mage counter...")
    counter = mage_counter()
    for i in range(1, 4):
        print(f"Call {i}: {counter()}")
    print()
    print("Testing spell accumulator...")
    accumulator = spell_accumulator(100)
    for power in power_additions:
        print(f"Accumulated power: {accumulator(power)}")
    print()
    print("Testing enchantment factory...")
    factory_list = [enchantment_factory(enchantment)
                    for enchantment in enchantment_types]
    for item, factory in zip(items_to_enchant, factory_list):
        print(f"{factory(item)}")
    print()
    print("Testing memory vault...")
    vault = memory_vault()
    vault["store"]("Fireball", "fire")
    print(f"Looking for Fireball: {vault['recall']('Fireball')}")
    print(f"Looking for Sword: {vault['recall']('Sword')}")


if __name__ == "__main__":
    main()
