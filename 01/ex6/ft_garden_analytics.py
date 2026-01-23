class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self, cm):
        self.height += cm
        return f"{self.name} grew {cm}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.is_blooming = True

    def __str__(self):
        status = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points

    def __str__(self):
        return f"{super().__str__()}, Prize points: {self.points}"


class GardenManager:
    total_gardens = 0
    garden_scores = {}

    class GardenStats:
        @staticmethod
        def calculate_total(plants_growth_list):
            return sum(plants_growth_list)

        @staticmethod
        def count_types(plants):
            stats = {"regular": 0, "flowering": 0, "prize": 0}
            for p in plants:
                if isinstance(p, PrizeFlower):
                    stats["prize"] += 1
                elif isinstance(p, FloweringPlant):
                    stats["flowering"] += 1
                elif isinstance(p, Plant):
                    stats["regular"] += 1
            return stats

    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.plants = []
        self.growth_history = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def maintain_garden(self, cm):
        print(f"\n{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            print(plant.grow(cm))
            self.growth_history.append(cm)

    @staticmethod
    def validate_height(height):
        return height > 0

    @classmethod
    def create_garden_network(cls):
        scores_str = ", ".join([f"{name}: {score}" for name,
                                score in cls.garden_scores.items()])
        print(f"Garden scores - {scores_str}")
        print(f"Total gardens managed: {cls.total_gardens}")

    def generate_report(self):
        print(f"\n=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        current_score = 0

        for p in self.plants:
            if isinstance(p, (PrizeFlower, FloweringPlant)):
                print(f"- {p}")
                current_score += p.height + (getattr(p, 'points', 0)) + 15
            else:
                print(f"- {p.name}: {p.height}cm")
                current_score += p.height
            valid = self.validate_height(p.height)
        GardenManager.garden_scores[self.owner_name] = current_score
        stats = self.GardenStats.count_types(self.plants)
        total_growth = self.GardenStats.calculate_total(self.growth_history)

        print(f"\nPlants added: {len(self.plants)},", end="")
        print(f" Total growth: {total_growth}cm")
        print(f"Plant types: {stats['regular']} regular, ", end="")
        print(f"{stats['flowering']} flowering, ", end="")
        print(f"{stats['prize']} prize flowers")
        print(f"\nHeight validation test: {valid}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")
    GardenManager.garden_scores["Bob"] = 92
    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    alice_garden.maintain_garden(1)
    alice_garden.generate_report()
    GardenManager.create_garden_network()
