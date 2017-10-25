"""Main entry point for the package."""
from .config import Configurator


def main():
    """Entry point for main module."""
    configurator = Configurator()
    configurator.parse()


if __name__ == '__main__':
    main()
