class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color: str = color
        print(f"{self.name} (Flower): {self.height}cm,", end="")
        print(f" {self.age} days, {self.color} color")

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter
        print(f"{self.name} (Tree): {self.height}cm,", end="")
        print(f" {self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self):
        shade: int = self.trunk_diameter * 1.5
        print(f"{self.name} provides {int(shade)} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value
        print(f"{self.name} (Vegetable): {self.height}cm,", end="")
        print(f" {self.age} days, {self.harvest_season} harvest")

    def get_nutrition(self):
        print(f"{self.name} is rich in {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")
    print()

    rose: Flower = Flower("Rose", 25, 30, "red")
    rose.bloom()
    print()

    oak: Tree = Tree("Oak", 500, 1825, 50)
    oak.produce_shade()
    print()

    tomato: Vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    tomato.get_nutrition()
    print()

    lila: Flower = Flower("Lila", 15, 20, "purple")
    lila.bloom()
    print()

    spruce: Tree = Tree("Spruce", 750, 2125, 40)
    spruce.produce_shade()
    print()

    strawberry: Vegetable = Vegetable("Strawberry", 90, 80, "may", "vitamin C")
    strawberry.get_nutrition()
    print()

    print("=== End of Program ===")


if __name__ == "__main__":
    main()
