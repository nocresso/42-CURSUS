#!/usr/bin/env python3

def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


plants = ["tomato", "lettuce", "carrots"]
plant_error = ["tomato", None]


def test_watering_system():
    print("=== Garden Watering System ===")
    try:
        print("\nTesting normal watering...")
        water_plants(plants)
        print("Watering completed succesfully!")
        print("\nTesting with error...")
        water_plants(plant_error)
    except Exception:
        pass
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
