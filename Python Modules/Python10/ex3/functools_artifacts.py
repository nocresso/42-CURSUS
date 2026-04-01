from typing import Dict, List
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: List[int], operation: str) -> int:
    if operation == "add":
        return reduce(add, spells)
    elif operation == "multiply":
        return reduce(mul, spells)
    elif operation == "max":
        return max(spells)
    elif operation == "min":
        return min(spells)
    else:
        raise ValueError("Invalid operation")


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} enchant with {power} power {target}"


def partial_enchanter(base_enchantment: callable) -> Dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning")
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Number cannot be negative")
    elif n <= 1:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> callable:
    @singledispatch
    def spell(arg) -> str:
        return "Unknown data. Not possible spell creation."

    @spell.register(int)
    def int_handler(arg: int) -> str:
        return f"Spell with {arg} damage was applied"

    @spell.register(str)
    def str_handler(arg: str) -> str:
        return f"Enchantment {arg} used"

    @spell.register(list)
    def list_handler(arg: list) -> str:
        return f"Spell targets: {', '.join(arg)}"

    return spell


def main() -> None:
    spell_powers = [11, 15, 38, 30, 34, 32]

    print("Testing spell reducer...")
    try:
        print(f"Sum: {spell_reducer(spell_powers, 'add')}")
        print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
        print(f"Max: {spell_reducer(spell_powers, 'max')}")
        print(f"Min: {spell_reducer(spell_powers, 'min')}")
    except Exception as e:
        print(f"Error: {e}")
    print()
    print("Testing partial enchanter...")
    try:
        partial_enchant = partial_enchanter(base_enchantment)
        print(f"{partial_enchant['fire_enchant']('sword')}")
    except Exception as e:
        print(f"Error: {e}")
    print()
    print("Testing memoized fibbonacci...")
    try:
        print(f"Fib(10): {memoized_fibonacci(10)}")
        print(f"Fib(15): {memoized_fibonacci(15)}")
    except Exception as e:
        print(f"Error: {e}")
    print()
    print("Testing spell dispatcher")
    try:
        spell = spell_dispatcher()
        print(f"Testing with int: {spell(15)}")
        print(f"Testing with str: {spell('Fireball')}")
        print(f"Testing with list: {spell(['goblin', 'dragon'])}")
        print(f"Testing with other type: {spell({'sword': '7'})}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
