from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(
    mages: list[dict[str, Any]], min_power: int
) -> list[dict[str, Any]]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    powers = list(map(lambda x: x["power"], mages))
    if not powers:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    return {
        "max_power": max(powers, key=lambda x: x),
        "min_power": min(powers, key=lambda x: x),
        "avg_power": round(sum(powers) / len(powers), 2),
    }


def main() -> None:
    artifacts = [
        {"name": "Fire Staff", "power": 92},
        {"name": "Crystal Orb", "power": 85},
    ]
    print("Testing artifact sorter...")
    sorted_art = artifact_sorter(artifacts)
    print(
        f"{sorted_art[0]['name']} ({sorted_art[0]['power']} power) "
        f"comes before {sorted_art[1]['name']}"
    )

    spells = ["fireball", "heal", "shield"]
    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells)))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
