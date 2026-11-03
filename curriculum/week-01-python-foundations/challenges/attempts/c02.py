"""audit.py -- print a summary of the current Python environment."""

import os
import platform
import sys
from importlib.metadata import distributions

RULE_WIDTH: int = 58


def is_in_virtualenv() -> bool:
    """Return True when running inside a venv."""
    is_env = sys.prefix != sys.base_prefix
    return is_env


def installed_packages() -> list[tuple[str, str]]:
    """Return (name, version) pairs for every installed distribution."""
    # TODO 2: walk importlib.metadata.distributions() and collect the
    #         name and version of each one, sorted, with no duplicates.
    found: dict[str, str] = {}
    for dist in distributions():
        name: str = dist.metadata["Name"] or ""
        if name and name not in found:
            found[name] = dist.version
    return sorted(found.items(), key=lambda pair: pair[0].lower())


def main() -> None:
    """Print the whole audit to standard output."""
    print("=" * RULE_WIDTH)
    print(" Python Environment Audit")
    print("=" * RULE_WIDTH)
    print(f"Python version : {platform.python_version()}")
    print(f"Implementation : {platform.python_implementation()}")
    print(f"Platform       : {platform.platform()}")
    print(f"Executable     : {sys.executable}")
    print(f"Current dir    : {os.getcwd()}")
    print(f"Inside env?    : {'yes' if is_in_virtualenv() else 'no'}")

    packages: list[tuple[str, str]] = installed_packages()
    print()
    print(f"Installed packages ({len(packages)}):")
    if not packages:
        print("  (none)")
    else:
        width: int = max(len(name) for name, _ in packages)
        for name, version in packages:
            print(f"  - {name.ljust(width)}  {version}")
    print("=" * RULE_WIDTH)

if __name__ == "__main__":
    main()
