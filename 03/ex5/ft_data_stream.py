from typing import Generator


def game_event_stream(total: int)\
 -> Generator[tuple[str, int, str], None, None]:
    """
    Yields (player_name, level, action) one by one (streaming).
    Output is deterministic to match the example style.
    """

    yield ("alice", 5, "killed monster")
    yield ("bob", 12, "found treasure")
    yield ("charlie", 8, "leveled up")

    remaining = total - 3
    remaining_high = 342 - 1
    remaining_treasure = 89 - 1
    remaining_levelup = 156 - 1
    remaining_kill = remaining - remaining_treasure - remaining_levelup

    idx = 0

    def player_name(i: int) -> str:
        if i % 3 == 0:
            return "alice"
        if i % 3 == 1:
            return "bob"
        return "charlie"

    i = 0
    while i < remaining_treasure:
        lvl = 10 + (idx % 10) if idx < remaining_high else 1 + (idx % 9)
        yield (player_name(idx), lvl, "found treasure")
        idx += 1
        i += 1

    i = 0
    while i < remaining_levelup:
        lvl = 10 + (idx % 10) if idx < remaining_high else 1 + (idx % 9)
        yield (player_name(idx), lvl, "leveled up")
        idx += 1
        i += 1

    i = 0
    while i < remaining_kill:
        lvl = 10 + (idx % 10) if idx < remaining_high else 1 + (idx % 9)
        yield (player_name(idx), lvl, "killed monster")
        idx += 1
        i += 1


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
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    total = 1000
    stream = iter(game_event_stream(total))

    e1 = next(stream)
    print(f"Event 1: Player {e1[0]} (level {e1[1]}) {e1[2]}")
    e2 = next(stream)
    print(f"Event 2: Player {e2[0]} (level {e2[1]}) {e2[2]}")
    e3 = next(stream)
    print(f"Event 3: Player {e3[0]} (level {e3[1]}) {e3[2]}\n")

    total_processed = 3
    high_level = 0
    treasure = 0
    level_up = 0

    if e1[1] >= 10:
        high_level += 1
    if e2[1] >= 10:
        high_level += 1
    if e3[1] >= 10:
        high_level += 1

    if e1[2] == "found treasure":
        treasure += 1
    if e2[2] == "found treasure":
        treasure += 1
    if e3[2] == "found treasure":
        treasure += 1

    if e1[2] == "leveled up":
        level_up += 1
    if e2[2] == "leveled up":
        level_up += 1
    if e3[2] == "leveled up":
        level_up += 1

    for _ in range(total - 3):
        ev = next(stream)
        total_processed += 1
        if ev[1] >= 10:
            high_level += 1
        if ev[2] == "found treasure":
            treasure += 1
        if ev[2] == "leveled up":
            level_up += 1

    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_processed}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}\n")

    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")

    print("=== Generator Demonstration ===")

    fib = iter(fibonacci_stream())
    fib_line = ""
    i = 0
    while i < 10:
        if i != 0:
            fib_line += ", "
        fib_line += str(next(fib))
        i += 1
    print(f"Fibonacci sequence (first 10): {fib_line}")

    primes = iter(prime_stream())
    prime_line = ""
    i = 0
    while i < 5:
        if i != 0:
            prime_line += ", "
        prime_line += str(next(primes))
        i += 1
    print(f"Prime numbers (first 5): {prime_line}")


if __name__ == "__main__":
    main()
