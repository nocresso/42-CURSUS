#! /usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height = self.height + 1

    def aging(self) -> None:
        self.age = self.age + 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)


def main():
    print("=== Day 1 ===")
    print(rose.get_info())
    print(sunflower.get_info())
    print("=== Day 7 ===")
    initial_rheight = rose.height
    initial_sheight = sunflower.height
    for day in range(1, 7):
        rose.grow()
        rose.aging()
        sunflower.grow()
        sunflower.aging()
    print(rose.get_info())
    print(f"Growth this week: +{rose.height - initial_rheight}cm")
    print(sunflower.get_info())
    print(f"Growth this week: +{sunflower.height - initial_sheight}cm")


if __name__ == "__main__":
    main()
