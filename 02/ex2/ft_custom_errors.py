class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant_status(plant_name):
    raise PlantError(f"The {plant_name} plant is wilting!")


def check_water_level(water_amount):
    if water_amount < 5:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")

    try:
        print("Testing PlantError...")
        check_plant_status("tomato")
    except PlantError as e:
        print("Caught PlantError:", e)

    print()

    try:
        print("Testing WaterError...")
        check_water_level(0)
    except WaterError as e:
        print("Caught WaterError:", e)

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

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
