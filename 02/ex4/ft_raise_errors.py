def check_plant_health(name: str, water_level: int, hours: int) -> str:
    if name == "":
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high")

    if hours < 2:
        raise ValueError(f"Sunlight hours {hours} is too low")
    if hours > 12:
        raise ValueError(f"Sunlight hours {hours} is too high")

    return f"Plant '{name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")

    try:
        print("Testing good values...")
        msg = check_plant_health("tomato", 5, 6)
        print(msg)
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)

    print()

    try:
        print("Testing empty plant name...")
        msg = check_plant_health("", 5, 6)
        print(msg)
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)

    print()

    try:
        print("Testing bad water level...")
        msg = check_plant_health("tomato", 15, 6)
        print(msg)
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)

    print()

    try:
        print("Testing bad sunlight hours...")
        msg = check_plant_health("tomato", 5, 0)
        print(msg)
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)

    print("\nAll error raising tests completed!")
    print()
    print("=== End of Program ===")


if __name__ == "__main__":
    test_plant_checks()
