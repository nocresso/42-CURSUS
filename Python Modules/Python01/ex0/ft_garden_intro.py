#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


rose = Plant("Rose", 25, 30)


def main():
    print("=== Welcome to my Garden ===")
    print(f"Plant: {rose.name}")
    print(f"Height: {rose.height}cm")
    print(f"Age: {rose.age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    main()
