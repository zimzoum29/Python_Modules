class GardenError(Exception):
    error_msg = "Garden Error !"

    def __init__(self, msg: str = None) -> None:
        super().__init__(msg if msg is not None else self.error_msg)


class PlantError(GardenError):
    error_msg = "Plant Error !"


class WaterError(GardenError):
    error_msg = "Water Error !"


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant_name: str) -> None:
        if plant_name == "":
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self) -> None:
        print("\nWatering plants...")
        print("Opening watering system")

        try:
            for plant in self.plants:
                if plant is None or plant == "":
                    raise PlantError("Cannot water invalid plant!")
                print(f"Watering {plant} - success")
        except PlantError as e:
            print("Error watering plants:", e)
        except Exception as e:
            print("Error:", e)
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name: str, water_level: int, hours: int,
                           ) -> None:
        if name == "":
            raise PlantError("Plant name cannot be empty!")

        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")

        if hours < 2:
            raise ValueError(f"Sunlight hours {hours} is too low (min 2)")
        if hours > 12:
            raise ValueError(f"Sunlight hours {hours} is too high (max 12)")

        print(f"{name}: healthy (water: {water_level}, sun: {hours})")

    def use_water_tank(self, amount_needed: int) -> None:
        if amount_needed > 0 and amount_needed > 5:
            raise WaterError("Not enough water in tank!")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")

    gm = GardenManager()

    print("Adding plants to garden...")
    try:
        gm.add_plant("tomato")
        gm.add_plant("lettuce")
        gm.add_plant("")
    except PlantError as e:
        print("Error adding plant:", e)
    except Exception as e:
        print("Error:", e)

    gm.water_plants()

    print("\nChecking plant health...")
    try:
        gm.check_plant_health("tomato", 5, 8)
    except (PlantError, ValueError) as e:
        print("Error checking tomato:", e)
    except Exception as e:
        print("Error:", e)

    try:
        gm.check_plant_health("lettuce", 15, 8)
    except (PlantError, ValueError) as e:
        print("Error checking lettuce:", e)
    except Exception as e:
        print("Error:", e)

    print("\nTesting error recovery...")
    try:
        gm.use_water_tank("test")
    except GardenError as e:
        print("Caught GardenError:", e)
    except Exception as e:
        print("Error:", e)

    print("System recovered and continuing...\n")
    print("Garden management system test complete!")
    print()
    print("=== End of Program ===")


if __name__ == "__main__":
    test_garden_management()
