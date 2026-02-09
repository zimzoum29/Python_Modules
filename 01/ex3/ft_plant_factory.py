from typing import List, Tuple


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


class Factory:
    def create_plant(data: Tuple[str, int, int]) -> Plant:
        return Plant(data[0], data[1], data[2])


def main() -> None:
    plants_data: List[Tuple[str, int, int]] = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    count: int = 0

    for data in plants_data:
        Factory.create_plant(data)
        count += 1

    print(f"Total plants created: {count}")

    print("=== End of Program ===")


if __name__ == "__main__":
    main()
