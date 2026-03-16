import sys


def dict_lookup(item: str, dictionary: dict) -> bool:
    if item in dictionary:
        return True
    else:
        return False


def main() -> None:
    args = len(sys.argv)
    if args < 2:
        print("Error: Incorrect input for the program")
        return
    print("=== Inventory System Analysis ===")
    inventory = dict()
    for arg in sys.argv[1:]:
        try:
            item, quantity = arg.split(":")
            inventory[item] = int(quantity)
        except ValueError:
            print("Error: Incorrect input for the program")
            return
    total_items = sum(inventory.values())
    unique_items = len(inventory)
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}")

    print("\n=== Current Inventory ===")
    for item, quantity in inventory.items():
        percent = quantity / total_items * 100
        print(f"{item}: {quantity} units ({percent:.1f}%)")

    print("\n=== Inventory Statistics ===")
    max_value = max(inventory.values())
    min_value = min(inventory.values())
    max_item = max(inventory, key=inventory.get)
    min_item = min(inventory, key=inventory.get)
    print(f"Most abundant: {max_item} ({max_value} units)")
    print(f"Least abundant: {min_item} ({min_value} units)")

    print("\n=== Item Categories ===")
    categorized = {
        "moderate": {},
        "scarce": {}
    }

    for item, quantity in inventory.items():
        if quantity >= 5:
            categorized["moderate"].update({item: quantity})
        else:
            categorized["scarce"].update({item: quantity})
    print(f"Moderate: {categorized['moderate']}")
    print(f"Scarce: {categorized['scarce']}")

    print("\n=== Management Suggestions ===")
    restock = list()
    for item, quantity in inventory.items():
        if quantity <= 1:
            restock.append(item)
    print(f"Restock needed: {', '.join(restock)}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(inventory.keys())}")
    print("Dictionary values:"
          f" {', '.join(str(v) for v in inventory.values())}")
    item_look = "sword"
    print(f"Sample lookup - '{item_look}' in inventory:"
          f" {dict_lookup(item_look, inventory)}")


if __name__ == "__main__":
    main()
