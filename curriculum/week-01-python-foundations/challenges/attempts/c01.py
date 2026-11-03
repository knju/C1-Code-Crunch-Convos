"""banner.py -- print a name centered inside a box of ASCII characters."""

import sys

DEMO_NAME: str = "Ada"


def build_banner(name: str, padding: int = 6, border: str = "*") -> str:
    """Return the multi-line banner for a name as one string.

    Args:
        name: the text to centre, already trimmed.
        padding: spaces between the name and each border column.
        border: the single character the box is drawn with.

    Returns:
        Five lines joined by newlines: edge, blank, name, blank, edge.
    """
    inner_width: int = len(name) + 2 * padding
    edge: str = border * (inner_width + 2)
    blank: str = f"{border}{' ' * inner_width}{border}"
    middle: str = f"{border}{name.center(inner_width)}{border}"

    banner: str = "\n".join([edge, blank, middle, blank, edge])
    return banner


def read_name(argv: list[str]) -> str:
    """Return the name to draw, trimmed of the spaces around it."""
    username: str = " ".join(argv).strip()

    return username or DEMO_NAME


def main() -> None:
    """Read one name from the command line and print its banner."""
    print(build_banner(read_name(sys.argv[1:])))


if __name__ == "__main__":
    main()
