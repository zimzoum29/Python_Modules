from .elements import create_air, create_earth, create_fire, create_water


def healing_potion():
    return "Healing potion brewed with {} and {}".format(
        create_fire(),
        create_water(),
    )


def strength_potion():
    return "Strength potion brewed with {} and {}".format(
        create_earth(),
        create_fire(),
    )


def invisibility_potion():
    return "Invisibility potion brewed with {} and {}".format(
        create_air(),
        create_water(),
    )


def wisdom_potion():
    return "Wisdom potion brewed with all elements: {}, {}, {}, {}".format(
        create_fire(),
        create_water(),
        create_earth(),
        create_air(),
    )
