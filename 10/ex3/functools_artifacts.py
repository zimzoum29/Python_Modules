from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation == "add":
        return sum(spells)

    if operation == "multiply":
        return reduce(operator.mul, spells)

    if operation == "max":
        return max(spells)

    if operation == "min":
        return min(spells)

    raise ValueError("Unknown operation")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def dispatch(arg):
        return "Unknown spell type"

    @dispatch.register
    def _(arg: int):
        return f"Damage spell: {arg} damage"

    @dispatch.register
    def _(arg: str):
        return f"Enchantment: {arg}"

    @dispatch.register
    def _(arg: list):
        return f"Multi-cast: {len(arg)} spells"

    return dispatch


def main() -> None:
    print()
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print()
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print()
    print("Testing spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch(["ice", "fire", "lightning"]))
    print(dispatch((1, 2, 3)))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
