def ft_water_reminder() -> None:
    age: int = input("Days since last watering: ")
    if (int(age) > 2):
        print("Water the plants!")
    else:
        print("Plant are fine")
