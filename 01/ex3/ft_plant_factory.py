class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def display(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    names: list[str] = ["Rose", "Oak", "Cactus", "Sunflower", "Fern"]
    heights: list[int] = [25, 200, 5, 80, 15]
    ages: list[int] = [30, 365, 90, 45, 120]
    count: int = 0
    print("=== Plant Factory Output ===")
    for i in range(5):
        plant: Plant = Plant(names[i], heights[i], ages[i])
        plant.display()
        count += 1
    print()
    print(f"Total plants created: {count}")
