#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 360),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 145),
        ("Fern", 15, 120)
        ]


def main():
    print("=== Plant Factory Output ===")
    plants = []
    for plant in plant_data:
        name, height, age = plant
        new_plant = Plant(name, height, age)
        plants.append(new_plant)
        print(f"Created: {new_plant.name} ({new_plant.height}cm,"
              f" {new_plant.age} days)")
    count = 0
    for plant in plants:
        count += 1
    print(f"\nTotal plants created: {count}")


if __name__ == "__main__":
    main()
