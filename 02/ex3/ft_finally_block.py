def water_plants(plant_list: list[str]) -> None:
    print("Opening watering system")

    try:
        for plant in plant_list:
            if plant is None or plant == "":
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")

        print("Watering completed successfully!")

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print("Error:", e)

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    good_plants: list[str] = ["tomato", "lettuce", "carrots"]
    water_plants(good_plants)

    print()

    print("Testing with error...")
    bad_plants: list[str] = ["tomato", None, "carrots"]
    water_plants(bad_plants)

    print("\nCleanup always happens, even with errors!")
    print()
    print("=== End of Program ===")


if __name__ == "__main__":
    test_watering_system()
