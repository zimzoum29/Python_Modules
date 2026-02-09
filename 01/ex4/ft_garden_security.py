class SecurePlant:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.__height: int = 0
        self.__age: int = 0
        print(f"Plant created: {name}")

    def set_height(self, height: int) -> None:
        if height < 0:
            print("Invalid operation attempted: ", end="")
            print(f"height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print("Invalid operation attempted: ", end="")
            print(f"age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def display(self) -> None:
        print(f"Current plant: {self.name}", end="")
        print(f" ({self.get_height()}cm, {self.get_age()} days)")


def main() -> None:
    print("=== Garden Security System ===")
    print()

    plant: SecurePlant = SecurePlant("Rose")
    plant.set_height(25)
    plant.set_age(30)
    print()

    plant.set_height(-5)
    print()

    plant.display()

    print()
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
