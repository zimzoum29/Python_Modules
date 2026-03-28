def record_spell(spell_name, ingredients):
    from .validator import validate_ingredients

    validation = validate_ingredients(ingredients)
    if validation.endswith("VALID"):
        return "Spell recorded: {} ({})".format(spell_name, validation)
    return "Spell rejected: {} ({})".format(spell_name, validation)
