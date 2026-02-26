def validate_ingredients(ingredients):
    lowered = ingredients.lower()
    valid = ("fire" in lowered) or ("water" in lowered) or ("earth" in lowered) or ("air" in lowered)

    if valid:
        return "{} - VALID".format(ingredients)
    return "{} - INVALID".format(ingredients)