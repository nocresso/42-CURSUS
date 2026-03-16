#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age


def main():
    rose = SecurePlant("Rose", 25, 30)
    print("=== Garden Security System ===")
    print(f"Plant created: {rose.name}")
    print(f"Height updated: {rose.get_height()}cm [OK]")
    print(f"Age updated: {rose.get_age()} days [OK]\n")
    rose.set_height(-5)
    print(f"\nCurrent plant: {rose.name} ({rose.get_height()}cm,"
          f" {rose.get_age()} days)")


if __name__ == "__main__":
    main()
