def garden_operations(nbr_str: str) -> None:
    data = {"abc": "rose", "0": "oak", "1": "sunflower"}
    data = data[nbr_str]
    nbr = int(nbr_str)
    nbr = 100 / nbr
    tab = {"1": "file.txt", "2": "test.txt", "3":  "data,txt"}
    open(tab[nbr_str])


def test_error_types():
    print("=== Garden Error Types Demo ===\n")

    try:
        print("Testing ValueError...")
        garden_operations("abc")
    except ValueError as e:
        print("Caught ValueError:", e)

    try:
        print("\nTesting ZeroDivisionError...")
        garden_operations("0")
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)

    try:
        print("\nTesting FileNotFoundError...")
        garden_operations("1")
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)

    try:
        print("\nTesting KeyError...")
        garden_operations("missing_plant")
    except KeyError as e:
        print("Caught KeyError:", e)

    try:
        print("\nTesting multiple errors together...")
        garden_operations("abc")
        garden_operations("0")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Caught an error: {e}, but program continues!")

    print("\nAll error types tested successfully!")
    print()
    print("=== End of Program ===")


if __name__ == "__main__":
    test_error_types()
