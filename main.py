from typing import Dict, List

import yaml

from src.pages.home import ScreenManager


def load_configs(filename: str = "config.yaml") -> Dict[str, List]:
    """
    Load and return the user specific configs.
    """
    with open(filename, "r") as f:
        return yaml.safe_load(f)


def main() -> None:
    configs = load_configs()
    display = ScreenManager()
    display.run(palette=configs["palette"])


if __name__ == "__main__":
    main()
