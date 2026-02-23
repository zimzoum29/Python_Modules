from typing import Generator


def game_event_stream(total: int) -> Generator[tuple[str, int, str], None, None]:
    
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(total):
        player = players[i % len(players)]
        level = (i % 20) + 1
        action = actions[i % len(actions)]
        yield (player, level, action)


def fibonacci_stream() -> Generator[int, None, None]:
    """Infinite Fibonacci generator."""
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def prime_stream() -> Generator[int, None, None]:
    n = 2
    while True:
        is_prime = True
        d = 2
        while d * d <= n:
            if n % d == 0:
                is_prime = False
                break
            d += 1
        if is_prime:
            yield n
        n += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")

    total = 1000
    print(f"\nProcessing {total} game events...\n")

    stream = iter(game_event_stream(total))

    for i in range(3):
        event = next(stream)
        print(f"Event {i + 1}: {event}")

    high_level_count = 0
    treasure_count = 0
    levelup_count = 0

    for _ in range(total - 3):
        player, level, action = next(stream)

        if level >= 10:
            high_level_count += 1

        if action == "found treasure":
            treasure_count += 1
        elif action == "leveled up":
            levelup_count += 1

    print("\n--- Analytics ---")
    print(f"High-level events (>=10): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")

    print("\nMemory usage: Constant (streaming)")


if __name__ == "__main__":
    main()