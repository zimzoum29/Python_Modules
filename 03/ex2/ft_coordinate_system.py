import math


def distance_3d(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(coord_str):
    parts = coord_str.split(",")
    if len(parts) != 3:
        raise ValueError("Coordinates must have 3 values separated by commas")

    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])
    return (x, y, z)


def main():
    print("=== Game Coordinate System ===\n")

    position = (10, 20, 5)
    print(f"Position created: {position}")

    origin = (0, 0, 0)
    dist = distance_3d(origin, position)
    print(f"Distance between {origin} and {position}: {round(dist, 2)}\n")

    coord_str = "3,4,0"
    print(f'Parsing coordinates: "{coord_str}"')
    try:
        parsed = parse_coordinates(coord_str)
        print(f"Parsed position: {parsed}")
        dist2 = distance_3d(origin, parsed)
        print(f"Distance between {origin} and {parsed}: {dist2}\n")
    except ValueError as e:
        print("Error parsing coordinates:", e)
        print("Error details - Type:", type(e).__name__ + ",", "Args:", e.args)
        print()
    except Exception as e:
        print("Error:", e)

    bad_str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{bad_str}"')
    try:
        parsed_bad = parse_coordinates(bad_str)
        print(f"Parsed position: {parsed_bad}")
    except ValueError as e:
        print("Error parsing coordinates:", e)
        print("Error details - Type:", type(e).__name__ + ",", "Args:", e.args)
        print()
    except Exception as e:
        print("Error:", e)

    print("Unpacking demonstration:")
    x, y, z = parse_coordinates("3,4,0")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
