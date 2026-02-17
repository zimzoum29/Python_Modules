class GardenError(Exception):
    error_msg = "Garden Error !"

    def __init__(self, msg: str = None) -> None:
        super().__init__(msg if msg is not None else self.error_msg)


class PlantError(GardenError):
    error_msg = "Plant Error !"


class WaterError(GardenError):
    error_msg = "Water Error !"


def check_plant_status(plant_name: str) -> None:
    raise PlantError(f"The {plant_name} plant is wilting!")


def check_water_level(water_amount: int) -> None:
    if water_amount < 5:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    try:
        print("Testing PlantError...")
        check_plant_status("tomato")
    except PlantError as e:
        print("Caught PlantError:", e)
    except Exception as e:
        print("Error:", e)

    print()

    try:
        print("Testing WaterError...")
        check_water_level(0)
    except WaterError as e:
        print("Caught WaterError:", e)
    except Exception as e:
        print("Error:", e)

    print()

    print("Testing catching all garden errors...")
    for i in range(2):
        try:
            if i == 0:
                check_plant_status("tomato")
            else:
                check_water_level(0)
        except GardenError as e:
            print("Caught a garden error:", e)
        except Exception as e:
            print("Error:", e)

    print("\nAll custom error types work correctly!")
    print()
    print("=== End of Program ===")


if __name__ == "__main__":
    test_custom_errors()
