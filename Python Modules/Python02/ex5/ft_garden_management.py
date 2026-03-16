#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name = name
        self.water = water
        self.sun = sun


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, plant: "Plant") -> None:
        try:
            self.check_name(plant)
            self.plants.append(plant)
            print(f"Added {plant.name} succesfully")
        except ValueError as e:
            print(f"Error adding plant: {e}")

    def water_plant(self):
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_name(self, plant: Plant) -> None:
        if plant.name == "":
            raise ValueError("Plant name cannot be empty!")

    def check_plant_health(self, plant: Plant) -> None:
        if plant.water > 10:
            raise WaterError(f"Water level {plant.water} is too high (max 10)")
        elif plant.water < 1:
            raise WaterError("Not enough water in tank")
        elif plant.sun < 2:
            raise PlantError(f"Sunlight hours {plant.sun} is too low (min 2)")
        elif plant.sun > 12:
            raise PlantError(f"Sunlight hours {plant.sun}"
                             " is too high (max 12)")


def test_garden_management():
    manager = GardenManager()

    plant_data = [
        ("tomato", 5, 8),
        ("lettuce", 15, 5),
        ("", 5, 90),
        ]

    print("=== Garden Management System ===")
    print("\nAdding plants to garden...")
    for name, water, sun in plant_data:
        plant = Plant(name, water, sun)
        manager.add_plant(plant)
    print("\nWatering plants...")
    manager.water_plant()
    print("\nChecking plant health...")
    for plant in manager.plants:
        try:
            manager.check_plant_health(plant)
            print(f"{plant.name}: healthy (water:"
                  f" {plant.water}, sun: {plant.sun})")
        except GardenError as e:
            print(f"Error checking {plant.name}: {e}")
    print("\nTesting error recovery...")
    carrot = Plant("carrot", 0, 5)
    try:
        manager.check_plant_health(carrot)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
