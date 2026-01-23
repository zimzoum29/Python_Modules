class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.days: int = age

    def grow(self):
        self.height += 1

    def age(self):
        self.days += 1

    def get_status(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old")


if __name__ == "__main__":
    plant: Plant = Plant("Rose", 25, 30)
    start_height: int = plant.height
    print("=== Day 1 ===")
    plant.get_status()
    for _ in range(6):
        plant.grow()
        plant.age()
    print("=== Day 7 ===")
    plant.get_status()
    print("Growth this week: +" + str(plant.height - start_height) + "cm")
