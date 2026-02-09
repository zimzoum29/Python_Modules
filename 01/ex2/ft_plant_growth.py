class Plant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name: str = name
        self.height: int = height
        self.days: int = days

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.days += 1

    def get_status(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def main() -> None:
    plant = Plant("Rose", 25, 30)
    start_height = plant.height

    print("=== Day 1 ===")
    plant.get_status()
    for i in range(6):
        plant.grow()
        plant.age()

    print("=== Day 7 ===")
    plant.get_status()
    print(f"Growth this week: +{plant.height - start_height}cm")

    print()
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
