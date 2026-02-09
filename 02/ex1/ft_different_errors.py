def garden_operations(nbr_str: str) -> None:
    try:
        nbr = int(nbr_str)
        index = 100 / nbr
        open("file.txt")
        tab = tab[nbr]
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileExistsError:
        print("Caught FileNotFoundError: No such file 'file.txt'")
    except KeyError:
        print("Caught KeyError")
