#!/usr/bin/env python3

def check_temperature(temp_str):
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return
    if temp < 0:
        print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
        return
    if temp > 40:
        print(f"Error: {temp_str}°C is too hot for plants (mac 40°C)")
        return
    print(f"Temperature {temp_str}°C is perfect for plants!")
    return temp


def test_temperature_input():
    test_values = ["25", "abc", "100", "-50"]

    for value in test_values:
        print(f"\nTesting temperature: {value}")
        check_temperature(value)


def main():
    print("=== Garden Temperature Checker ===")
    test_temperature_input()
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
