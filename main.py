from src.display import DisplayManager
import urwid
import yaml


def exit_on_key(key: str) -> None:
    """
    Exits the application when certain keys are pressed.
    """
    if key in {"q", "Q"}:
        raise urwid.ExitMainLoop()


def load_configs(filename: str = "config.yaml"):
    """
    Load and return the user specific configs.
    """
    with open(filename, "r") as f:
        return yaml.safe_load(f)


def main() -> None:
    configs = load_configs()
    display = DisplayManager()
    display.start(palette=configs["palette"])


if __name__ == "__main__":
    main()
