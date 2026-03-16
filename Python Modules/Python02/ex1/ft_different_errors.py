#!/usr/bin/env python3

def garden_operations(error):
    if error == "value":
        try:
            int("abc")
        except ValueError:
            print("Caught ValueError: invalid literal for int()")
    elif error == "zero":
        try:
            res = 10 / 0
            print(f"{res}")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
    elif error == "file":
        try:
            open("missing.txt")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: No such file '{e.filename}'")
    elif error == "key":
        try:
            plants = {"tomato": 10}
            print(plants["carrot"])
        except KeyError as e:
            print(f"Caught KeyError: missing {e}")
    elif error == "multiple":
        try:
            int("")
        except (ValueError, ZeroDivisionError):
            print("Caught an error, but program continues!")


def test_error_types():
    print("\nTesting ValueError...")
    garden_operations("value")
    print("\nTesting ZeroDivisionError...")
    garden_operations("zero")
    print("\nTesting FileNotFoundError...")
    garden_operations("file")
    print("\nTesting KeyError...")
    garden_operations("key")
    print("\nTesting multiple errors together...")
    garden_operations("multiple")


def main():
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    main()
