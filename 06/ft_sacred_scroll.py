import alchemy


def main():
    print("=== Sacred Scroll Mastery ===\n")

    print("Direct module access:")
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print("alchemy.elements.create_water():", alchemy.elements.create_water())
    print("alchemy.elements.create_earth():", alchemy.elements.create_earth())
    print("alchemy.elements.create_air():", alchemy.elements.create_air())

    print("\nPackage-level access (via alchemy/__init__.py):")
    print("alchemy.create_fire():", alchemy.create_fire())
    print("alchemy.create_water():", alchemy.create_water())

    try:
        print("alchemy.create_earth():", alchemy.create_earth())
    except AttributeError as e:
        print("alchemy.create_earth(): AttributeError (not exposed)", e)

    try:
        print("alchemy.create_air():", alchemy.create_air())
    except AttributeError as e:
        print("alchemy.create_air(): AttributeError (not exposed)", e)

    print("\nMetadata:")
    print("Version:", alchemy.__version__)
    print("Author:", alchemy.__author__)


if __name__ == "__main__":
    main()
