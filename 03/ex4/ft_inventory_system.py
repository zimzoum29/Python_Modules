import sys


def parse_inventory_args(argv):
    inventory = dict()

    i = 1
    while i < len(argv):
        token = argv[i]

        parts = token.split(":")
        if len(parts) != 2:
            print(f"Invalid item ignored: {token}")
            i += 1
            continue

        name = parts[0]
        qty_str = parts[1]

        try:
            qty = int(qty_str)
        except ValueError:
            print(f"Invalid quantity ignored: {token}")
            i += 1
            continue

        current = inventory.get(name, 0)
        inventory.update({name: current + qty})

        i += 1

    return inventory


def total_quantity(inventory):
    total = 0
    for _, qty in inventory.items():
        total += qty
    return total


def print_keys_line(inventory):
    out = ""
    first = True
    for k in inventory.keys():
        if not first:
            out += ", "
        out += str(k)
        first = False
    print(out)


def print_values_line(inventory):
    out = ""
    first = True
    for v in inventory.values():
        if not first:
            out += ", "
        out += str(v)
        first = False
    print(out)


def main():
    inventory = parse_inventory_args(sys.argv)

    print("=== Inventory System Analysis ===")

    if len(inventory) == 0:
        print("No inventory provided. Usage: python3 ", end="")
        print("ft_inventory_system.py item:qty item:qty ...")
        return

    total_items = total_quantity(inventory)
    unique_types = len(inventory)

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_types}\n")

    print("=== Current Inventory ===")

    for name, qty in inventory.items():
        pct = (qty / total_items) * 100.0
        unit_word = "unit" if qty == 1 else "units"
        print(f"{name}: {qty} {unit_word} ({pct:.1f}%)")

    print("\n=== Inventory Statistics ===")

    most_item = max(inventory, key=inventory.get)
    least_item = min(inventory, key=inventory.get)
    most_qty = inventory.get(most_item)
    least_qty = inventory.get(least_item)

    most_word = "unit" if most_qty == 1 else "units"
    least_word = "unit" if least_qty == 1 else "units"

    print(f"Most abundant: {most_item} ({most_qty} {most_word})")
    print(f"Least abundant: {least_item} ({least_qty} {least_word})\n")

    print("=== Item Categories ===")

    moderate = dict()
    scarce = dict()

    for name, qty in inventory.items():
        if qty >= 5:
            moderate.update({name: qty})
        else:
            scarce.update({name: qty})

    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}\n")

    print("=== Management Suggestions ===")

    restock = []
    for name, qty in inventory.items():
        if qty == 1:
            restock.append(name)

    print(f"Restock needed: {restock}\n")

    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys: ", end="")
    print_keys_line(inventory)

    print("Dictionary values: ", end="")
    print_values_line(inventory)

    sample_key = "sword"
    print(f"Sample lookup - '{sample_key}' in inventory: ", end="")
    print(f"{inventory.get(sample_key) is not None}")


if __name__ == "__main__":
    main()
