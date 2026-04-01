from typing import Dict, List, Any


def artifact_sorter(artifacts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(artifacts, key=lambda artifact: artifact['power'],
                  reverse=True)


def power_filter(mages: List[Dict[str, Any]],
                 min_power: int) -> List[Dict[str, Any]]:
    filtered = list(filter(lambda mage: mage['power'] >= min_power, mages))
    return filtered


def spell_transformer(spells: List[str]) -> List[str]:
    spell_transformed = list(map((lambda spell: "* " + spell + " *"), spells))
    return spell_transformed


def mage_stats(mages: List[Dict[str, Any]]) -> Dict[str, Any]:
    max_power = max(mages, key=lambda mage: mage['power'])['power']
    min_power = min(mages, key=lambda mage: mage['power'])['power']
    total = sum(map(lambda mage: mage['power'], mages))
    average_power = total / len(mages)
    return {
        "max_power": max_power,
        "min_power": min_power,
        "average_power": average_power
    }


def main() -> None:
    artifacts = [{'name': 'Earth Shield', 'power': 90, 'type': 'accessory'},
                 {'name': 'Water Chalice', 'power': 105, 'type': 'weapon'},
                 {'name': 'Wind Cloak', 'power': 60, 'type': 'armor'},
                 {'name': 'Light Prism', 'power': 69, 'type': 'accessory'}]
    mages = [{'name': 'River', 'power': 78, 'element': 'fire'},
             {'name': 'Phoenix', 'power': 92, 'element': 'earth'},
             {'name': 'Luna', 'power': 50, 'element': 'earth'},
             {'name': 'Kai', 'power': 64, 'element': 'wind'},
             {'name': 'Luna', 'power': 82, 'element': 'shadow'}]
    spells = ['earthquake', 'freeze', 'meteor', 'tsunami']
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']}"
          f" power) comes before than {sorted_artifacts[1]['name']}"
          f" ({sorted_artifacts[1]['power']} power)")
    print()
    print("Testing spell transformer...")
    print(f"{' '.join(spell_transformer(spells))}")
    print()
    print("Testing power filter...")
    filtered_power = [f"{mage['name']}: {mage['power']}"
                      for mage in power_filter(mages, 70)]
    print(f"{', '.join(filtered_power)}")
    print()
    print("Testing mage_stats...")
    mages_stats = mage_stats(mages)
    for name, data in mages_stats.items():
        print(f"{name}: {data}")


if __name__ == "__main__":
    main()
