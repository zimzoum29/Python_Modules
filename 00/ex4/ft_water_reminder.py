def ft_water_reminder():
    age = input("Days since last watering: ")
    if (int(age) > 2):
        print("Water the plants!")
    else:
        print("Plant are fine")
