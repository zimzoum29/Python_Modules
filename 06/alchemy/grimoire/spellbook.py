def record_spell(spell_name, ingredients):
    # Late import: évite d’importer validator au moment où le module est importé
    from .validator import validate_ingredients

    validation = validate_ingredients(ingredients)
    if validation.endswith("VALID"):
        return "Spell recorded: {} ({})".format(spell_name, validation)
    return "Spell rejected: {} ({})".format(spell_name, validation)