#!/usr/bin/env python3

def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif water_level < 1:
        raise ValueError("Invalid water level (min 1)")
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours}"
                         " is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours}"
                         " is too high (max 12)")
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")
    try:
        print("\nTesting good values...")
        check_plant_health("tomato", 5, 5)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print("\nTesting empty plant name...")
        check_plant_health("", 5, 5)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print("\nTesting bad water level...")
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print("\nTesting bad sunlight hours...")
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
