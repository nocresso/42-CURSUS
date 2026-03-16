#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def basic_info(self) -> str:
        return (f"{self.name} ({self.__class__.__name__}):"
                f" {self.height}cm, {self.age} days")

    def special_action(self) -> None:
        pass


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!\n")

    def get_info(self) -> str:
        return f"{self.basic_info()}, {self.color} color"

    def special_action(self) -> None:
        self.bloom()


class Tree(Plant):
    def __init__(self, name: str, height: int,
                 age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade_area = self.height * 2
        print(f"{self.name} provides {shade_area} square meters of shade\n")

    def get_info(self) -> str:
        return f"{self.basic_info()}, {self.trunk_diameter}cm diameter"

    def special_action(self) -> None:
        self.produce_shade()


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> str:
        return (f"{self.basic_info()}, {self.harvest_season} harvest")

    def special_action(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}\n")


rose = Flower("Rose", 25, 30, "red")
sunflower = Flower("Sunflower", 30, 65, "yellow")
oak = Tree("Oak", 500, 1825, 50)
palmtree = Tree("Palm tree", 150, 365, 70)
tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
carrot = Vegetable("Carrot", 30, 20, "spring", "vitamin D")

plants = [rose, sunflower, oak, palmtree, tomato, carrot]


def main():
    print("=== Garden Plant Types ===")
    for plant in plants:
        print(plant.get_info())
        plant.special_action()


if __name__ == "__main__":
    main()
