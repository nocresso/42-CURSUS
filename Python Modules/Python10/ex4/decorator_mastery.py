from functools import wraps
import time
from typing import Any


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        before = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - before
        print(f"Spell completed in {elapsed_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func) -> Any:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            power_index = func.__code__.co_varnames.index("power")
            if args[power_index] >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func) -> Any:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if max_attempts <= 0:
                return "Not available attempts"
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying..."
                          f" (attempt {attempt + 1}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name):
            return True
        else:
            return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    spell_names = ['freeze', 'blizzard', 'Alex123', 'Jo']
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        return "Result: Fireball casted!"

    print(fireball())
    print()
    print("Testing power validator...")
    guild = MageGuild()
    print(guild.cast_spell('Lighting', 5))
    print(guild.cast_spell('Lightning', 15))
    print()
    print("Testing retry spell...")

    @retry_spell(3)
    def unstable_spell():
        raise Exception("fail")

    print(unstable_spell())
    print()
    print("Testing name validation...")
    for name in spell_names:
        print(f"{name}: {MageGuild.validate_mage_name(name)}")


if __name__ == "__main__":
    main()
