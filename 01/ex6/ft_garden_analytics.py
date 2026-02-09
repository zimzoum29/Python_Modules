from typing import List, Dict, Tuple


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height

    def grow(self) -> int:
        self.height += 1
        return 1

    def describe(self) -> str:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color: str = color
        self.blooming: bool = False

    def grow(self) -> int:
        growth: int = super().grow()
        self.blooming = True
        return growth

    def describe(self) -> str:
        status: str = " (blooming)" if self.blooming else ""
        return f"- {self.name}: {self.height}cm, {self.color} flowers{status}"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize_points: int)\
     -> None:
        super().__init__(name, height, color)
        self.prize_points: int = prize_points

    def describe(self) -> str:
        status: str = " (blooming)" if self.blooming else ""
        return (
            f"- {self.name}: {self.height}cm, {self.color} flowers{status}, "
            f"Prize points: {self.prize_points}"
        )


class GardenManager:
    _total_gardens_managed: int = 0

    class GardenStats:
        @staticmethod
        def total_growth(garden: "GardenManager.Garden") -> int:
            return garden.total_growth

        @staticmethod
        def count_type(garden: "GardenManager.Garden") -> Tuple[int, int, int]:
            regular: int = 0
            flowering: int = 0
            prize: int = 0

            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1

            return regular, flowering, prize

        @staticmethod
        def score(garden: "GardenManager.Garden") -> int:
            total_height: int = 0
            flowering_bonus: int = 0
            prize_points: int = 0

            for plant in garden.plants:
                total_height += plant.height
                if isinstance(plant, FloweringPlant):
                    flowering_bonus += 15
                if isinstance(plant, PrizeFlower):
                    prize_points += plant.prize_points

            return total_height + flowering_bonus + prize_points

    class Garden:
        def __init__(self, owner: str) -> None:
            self.owner: str = owner
            self.plants: List[Plant] = []
            self.total_growth: int = 0

        def add_plant(self, plant: Plant) -> None:
            self.plants.append(plant)
            print(f"Added {plant.name} to {self.owner}'s garden")

        def help_all_plants_grow(self) -> None:
            print(f"{self.owner} is helping all plants grow...")
            for plant in self.plants:
                growth: int = plant.grow()
                self.total_growth += growth
                print(f"{plant.name} grew {growth}cm")

        def report(self, stats: "GardenManager.GardenStats") -> None:
            print(f"=== {self.owner}'s Garden Report ===")
            print("Plants in garden:")
            for plant in self.plants:
                print(plant.describe())
            print()

            print(
                f"Plants added: {len(self.plants)}, "
                f"Total growth: {stats.total_growth(self)}cm"
            )

            regular, flowering, prize = stats.count_type(self)
            print(
                f"Plant types: {regular} regular, "
                f"{flowering} flowering, {prize} prize flowers"
            )

    def __init__(self) -> None:
        self.gardens: Dict[str, GardenManager.Garden] = {}

    def add_garden(self, owner: str) -> "GardenManager.Garden":
        garden = GardenManager.Garden(owner)
        self.gardens[owner] = garden
        GardenManager._total_gardens_managed += 1
        return garden

    @classmethod
    def create_garden_network(cls, owners: List[str]) -> "GardenManager":
        manager: GardenManager = cls()
        for owner in owners:
            manager.add_garden(owner)
        return manager

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0

    @classmethod
    def total_gardens_managed(cls) -> int:
        return cls._total_gardens_managed


def main() -> None:
    print("=== Garden Management System Demo ===")

    manager: GardenManager = GardenManager.create_garden_network(
        ["Pablo", "Rayan"])
    stats: GardenManager.GardenStats = GardenManager.GardenStats()

    pablo_garden: GardenManager.Garden = manager.gardens["Pablo"]
    rayan_garden: GardenManager.Garden = manager.gardens["Rayan"]

    pablo_garden.add_plant(Plant("Oak", 110))
    pablo_garden.add_plant(FloweringPlant("Rose", 35, "red"))
    pablo_garden.add_plant(PrizeFlower("Sunflower", 60, "yellow", 15))

    print()
    pablo_garden.help_all_plants_grow()
    print()
    pablo_garden.report(stats)
    print()

    rayan_garden.plants.append(Plant("Cactus", 92))

    print(f"Height validation test: {GardenManager.validate_height(10)}")
    print(
        f"Garden scores - Alice: {stats.score(pablo_garden)}, "
        f"Bob: {stats.score(rayan_garden)}"
    )
    print(f"Total gardens managed: {GardenManager.total_gardens_managed()}")


if __name__ == "__main__":
    main()
