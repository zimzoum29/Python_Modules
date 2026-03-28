from alchemy.elements import create_earth, create_fire


def lead_to_gold():
    return "Lead transmuted to gold using {}".format(create_fire())


def stone_to_gem():
    return "Stone transmuted to gem using {}".format(create_earth())
