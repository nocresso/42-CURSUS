#!/usr/bin/env python3

class GardenManager:
    total_gardens = 0

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant: "Plant") -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def report(self) -> None:
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")

        stats = self.GardenStats(self)
        stats.calculate_stats()

    def calculate_score(self) -> int:
        total = 0
        for plant in self.plants:
            total += plant.height
        return total

    class GardenStats:
        def __init__(self, manager: "GardenManager") -> None:
            self.manager = manager

        def calculate_stats(self) -> None:
            total_growth = 0
            plant_count = 0
            regular = 0
            flowering = 0
            prize = 0

            for plant in self.manager.plants:
                total_growth += 1
                plant_count += 1

                plant_type = plant.get_type()
                if plant_type == "regular":
                    regular += 1
                elif plant_type == "flowering":
                    flowering += 1
                elif plant_type == "prize":
                    prize += 1
            print(f"\nPlants added: {plant_count}, "
                  f"Total growth: {total_growth}cm")
            print(f"Plant types: {regular} regular, "
                  f"{flowering} flowering, {prize} prize flowers")

    @classmethod
    def create_garden_network(cls) -> None:
        print(f"Total gardens managed: {cls.total_gardens}")

    @staticmethod
    def validate_height(height: int) -> bool:
        if height < 0:
            return False
        return True


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"

    def get_type(self) -> str:
        return "regular"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int,
                 age: int, flower_color: str) -> None:
        super().__init__(name, height, age)
        self.flower_color = flower_color

    def bloom(self) -> str:
        return f"{self.flower_color} flowers (blooming)"

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.bloom()}"

    def get_type(self) -> str:
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int,
                 flower_color: str, prize_points: int) -> None:
        super().__init__(name, height, age, flower_color)
        self.prize_points = prize_points

    def get_info(self) -> str:
        return (f"{self.name}: {self.height}cm, {self.bloom()},"
                f" Prize points: {self.prize_points}")

    def get_type(self) -> str:
        return "prize"


def main() -> None:
    print("=== Garden Management System Demo ===\n")

    garden1 = GardenManager("Alice")
    garden2 = GardenManager("Bob")

    oak = Plant("Oak Tree", 100, 365)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 60, "yellow", 10)

    garden1.add_plant(oak)
    garden1.add_plant(rose)
    garden1.add_plant(sunflower)

    garden1.grow_all()
    garden1.report()

    score1 = garden1.calculate_score()

    print("\nHeight validation test:",
          GardenManager.validate_height(10))
    print(f"Garden scores - {garden1.owner}:"
          f" {score1}, {garden2.owner}: 92")
    GardenManager.create_garden_network()


if __name__ == "__main__":
    main()
