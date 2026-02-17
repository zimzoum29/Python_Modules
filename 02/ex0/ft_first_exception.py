def check_temperature(temp_str: str) -> int | None:
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None
    except Exception as e:
        print("Error:", e)
        return None
    if temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
    else:
        print(f"Temperature {temp}°C is perfect for plants!")
        return temp
    return None


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    check_temperature("25")
    print()
    check_temperature("abc")
    print()
    check_temperature("100")
    print()
    check_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")
    print()
    print("=== End of Program ===")


if __name__ == "__main__":
    test_temperature_input()
