#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(age, water):
    if age > 10:
        raise PlantError("The tomato plant is wilting!")
    elif water < 10:
        raise WaterError("Not enough water in the tank!")


def test_plant(error):
    if error == "plant":
        try:
            check_plant(15, 15)
        except PlantError as e:
            print(f"Caught PlantError: {e}")
    elif error == "water":
        try:
            check_plant(5, 5)
        except WaterError as e:
            print(f"Caught WaterError: {e}")
    elif error == "multiple1":
        try:
            check_plant(15, 15)
        except GardenError as e:
            print(f"Caught a garden error: {e}")
    elif error == "multiple2":
        try:
            check_plant(5, 5)
        except GardenError as e:
            print(f"Caught a garden error: {e}")


def main():
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    test_plant("plant")
    print("\nTesting WaterError...")
    test_plant("water")
    print("\nTesting catching all garden errors...")
    test_plant("multiple1")
    test_plant("multiple2")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
