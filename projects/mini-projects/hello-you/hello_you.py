"""hello_you.py — greet one person, by name, from the terminal.

Week 1 mini-project for Code Crunch Convos. Asks for a name and an
optional favorite programming language, then prints a single friendly
line. Run it with: python hello_you.py
"""

DEFAULT_NAME: str = "friend"
DEFAULT_LANGUAGE: str = "Python"


def prompt_user() -> tuple[str, str]:
    """Ask for a name and a favorite language and return both, cleaned.

    Returns:
        A pair of strings, name first. Each falls back to its DEFAULT_
        constant when the user types nothing but whitespace.
    """
    name = input("Your name: ").strip() or DEFAULT_NAME
    language = input("Your favourite language (Enter for Python): ").strip() or DEFAULT_LANGUAGE

    return name, language


def build_greeting(name: str, language: str) -> str:
    """Return the greeting line for name and language.

    build_greeting("Ada", "Python") returns
    'Hello, Ada! Welcome to Code Crunch Convos. May your Python be readable.'

    Args:
        name: the person's name, already stripped.
        language: their favorite language, already stripped.

    Returns:
        One line of text. This function never prints; main() does that.
    """

    return f"Hello, {name}! Welcome to Code Crunch Convos. May your {language} be readable."


def main() -> None:
    """Collect the two answers, build the greeting, and print it."""
    name, language = prompt_user()
    print(build_greeting(name, language))


if __name__ == "__main__":
    main()
