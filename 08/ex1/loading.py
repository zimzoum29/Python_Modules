import importlib


REQUIRED_LIBS = ["pandas", "numpy", "matplotlib"]


def check_dependencies():
    """Check if required libraries are installed"""
    print("Checking dependencies:\n")

    available = {}

    for lib in REQUIRED_LIBS:
        try:
            module = importlib.import_module(lib)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {lib} ({version}) - Ready")
            available[lib] = module
        except ImportError:
            print(f"[FAIL] {lib} not installed")
            available[lib] = None

    return available


def install_help():
    print("\nTo install dependencies:")
    print("pip install -r requirements.txt")
    print("or")
    print("poetry install\n")


def run_analysis(modules):
    """Run fake data analysis"""
    pandas = modules["pandas"]
    numpy = modules["numpy"]
    matplotlib = modules["matplotlib"]

    if not all([pandas, numpy, matplotlib]):
        print("\nMissing dependencies. Cannot run analysis.")
        install_help()
        return

    print("\nAnalyzing Matrix data...")

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    data = np.random.randn(1000)
    df = pd.DataFrame(data, columns=["values"])

    print("Processing 1000 data points...")

    df.hist()
    plt.title("Matrix Data Distribution")
    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():
    print("\nLOADING STATUS: Loading programs...\n")

    modules = check_dependencies()
    run_analysis(modules)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
