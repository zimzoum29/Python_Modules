class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self):
        shade: int = self.trunk_diameter * 1.56
        print(f"{self.name} provides {int(shade)} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def get_nutrition(self):
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    rose: Flower = Flower("Rose", 25, 30, "red")
    print(f"{rose.name} (Flower): {rose.height}cm,", end="")
    print(f" {rose.age} days, {rose.color} color")
    rose.bloom()
    print()
    oak: Tree = Tree("Oak", 500, 1825, 50)
    print(f"{oak.name} (Tree): {oak.height}cm,", end="")
    print(f" {oak.age} days, {oak.trunk_diameter}cm diameter")
    oak.produce_shade()
    print()
    tomato: Vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print(f"{tomato.name} (Vegetable): {tomato.height}cm,", end="")
    print(f" {tomato.age} days, {tomato.harvest_season} harvest")
    tomato.get_nutrition()
