from typing import Generator
from random import randint


def game_event_stream(
        total: int
        ) -> Generator[tuple[str, int, str], None, None]:

    players = ["rayan", "pablo", "matisse"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(total):
        player = players[randint(0, len(players) - 1)]
        level = randint(1, 20)
        action = actions[randint(0, len(actions) - 1)]
        yield (player, level, action)


def fibonacci_stream() -> Generator[int, None, None]:
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
    monster_count = 0

    for _ in range(total - 3):
        player, level, action = next(stream)

        if level >= 10:
            high_level_count += 1

        if action == "found treasure":
            treasure_count += 1
        elif action == "leveled up":
            levelup_count += 1
        elif action == "killed monster":
            monster_count += 1

    print("\n--- Analytics ---")
    print(f"High-level events (>=10): {high_level_count}")
    print(f"Monster events: {monster_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")

    print("\n--- Generator Demonstration ---")

    fib = iter(fibonacci_stream())
    fib_values = []
    for _ in range(10):
        fib_values.append(next(fib))
    print(f"Fibonacci first 10: {fib_values}")

    primes = iter(prime_stream())
    prime_values = []
    for _ in range(10):
        prime_values.append(next(primes))
    print(f"Prime numbers first 10: {prime_values}")


if __name__ == "__main__":
    main()
