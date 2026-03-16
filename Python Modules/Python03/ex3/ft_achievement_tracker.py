#!/usr/bin/env python3

def main() -> None:
    print("=== Achievement Tracker System ===\n")
    Alice_list = ["first_kill", "level_10", "treasure_hunter",
                  "speed_demon", "runt_fast"]
    Bob_list = ["first_kill", "level_10", "boss_slayer", "collector"]
    Charlie_list = ["level_10", "treasure_hunter", "boss_slayer",
                    "speed_demon", "perfectionist"]

    Alice = set(Alice_list)
    Bob = set(Bob_list)
    Charlie = set(Charlie_list)

    print(f"Player Alice achievements: {Alice}")
    print(f"Player Bob achievements: {Bob}")
    print(f"Player Charlie achievements: {Charlie}")

    print("\n=== Achievement Analytics ===")
    all_achievements = Alice.union(Bob).union(Charlie)
    total = len(all_achievements)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {total}")

    common = Alice.intersection(Bob).intersection(Charlie)
    Alice_unique = Alice.difference(Bob).difference(Charlie)
    Bob_unique = Bob.difference(Alice).difference(Charlie)
    Charlie_unique = Charlie.difference(Alice).difference(Bob)
    unique = Alice_unique.union(Bob_unique).union(Charlie_unique)

    print(f"\nCommon to all players: {common}")
    print(f"Rare achievements: {unique}")

    AB_common = Alice.intersection(Bob)
    print(f"\nAlice vs Bob common: {AB_common}")
    print(f"Alice unique: {Alice_unique}")
    print(f"Bob unique: {Bob_unique}")
    print(f"Charlie unique: {Charlie_unique}")


if __name__ == "__main__":
    main()
