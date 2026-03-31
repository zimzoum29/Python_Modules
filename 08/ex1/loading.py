import sys
import importlib


REQUIRED_LIBS = ["pandas", "numpy", "matplotlib"]


def check_dependencies() -> dict:
    results = {}

    for lib in REQUIRED_LIBS:
        try:
            module = importlib.import_module(lib)
            version = getattr(module, "__version__", "unknown")
            results[lib] = ("OK", version)
        except ImportError:
            results[lib] = ("MISSING", None)

    return results


def print_dependencies(status: dict) -> bool:
    print("Checking dependencies:")

    all_ok = True

    for lib, (state, version) in status.items():
        if state == "OK":
            print(f"[OK] {lib} ({version}) - Ready")
        else:
            print(f"[MISSING] {lib} - Install required")
            all_ok = False

    return all_ok


def run_analysis() -> None:
    import numpy
    import pandas
    import matplotlib.pyplot

    data = numpy.random.rand(1000)
    df = pandas.DataFrame(data, columns=["values"])
    matplotlib.pyplot.hist(df["values"], bins=30)
    matplotlib.pyplot.title("Matrix Data Distribution")
    matplotlib.pyplot.savefig("matrix_analysis.png")

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    deps = check_dependencies()
    ok = print_dependencies(deps)

    if not ok:
        print("\nInstall dependencies with:")
        print("pip install -r requirements.txt")
        print("or")
        print("poetry install")
        sys.exit(1)

    run_analysis()


if __name__ == "__main__":
    main()
