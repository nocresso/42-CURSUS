from typing import List


def fireball(arg: str) -> str:
    return f"Fireball hits {arg}"


def heal(arg: str) -> str:
    return f"Heals {arg}"


def damage(arg: str) -> str:
    return f"{arg} damaged"


def power(arg: int) -> int:
    return arg


def condition(n: int) -> bool:
    if n >= 10:
        return True
    else:
        return False


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda arg: (spell1(arg), spell2(arg))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda arg: base_spell(arg) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    return lambda arg: spell(arg) if condition(arg) else "Spell fizzled"


def spell_sequence(spells: List[callable]) -> callable:
    return lambda arg: [spell(arg) for spell in spells]


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {', '.join(combined('Dragon'))}")
    print()
    print("Testing power_amplifier...")
    num = 10
    amplified = power_amplifier(power, 3)
    print(f"Original: {power(num)}, Amplified: {amplified(num)}")
    print()
    print("Testing conditional caster...")
    casted = conditional_caster(condition, power)
    print(f"Condition true: {casted(10)}, condition false: {casted(5)}")
    print()
    print("Testing spell sequence...")
    spells = [fireball, heal, damage]
    casted_spells = spell_sequence(spells)
    print(f"Casted spells: {', '. join(casted_spells('Dragon'))}")


if __name__ == "__main__":
    main()
