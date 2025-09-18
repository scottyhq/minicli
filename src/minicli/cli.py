"""
Use argparse from Python standard library to handle command line arguments.
"""
from minicli.hdfutils import dump_datatree
import argparse

def app():
    """
    We call this "app" but it can be anything, the actual CLI name is
    defined in pyproject.toml under [project.scripts]
    """
    parser = argparse.ArgumentParser(description="Dump HDF5 file tree.")
    parser.add_argument("-i", "--input", type=str, required=True, help="Path to the HDF5 file")
    args = parser.parse_args()

    dump_datatree(args.input)


if __name__ == "__main__":
    app()
