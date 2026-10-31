"""exercise-03-script-vs-repl.py — one file, two ways to run it."""

SIGNUPS: list[str] = ["Ada", "Grace", "Katherine", "Dorothy", "Mary"]

def initials(names: list[str]) -> str:
    """Return each name's first letter, joined by single spaces."""
    # TODO: "Ada", "Grace" -> "A G". Empty list -> "".
    result = []
    for name in names:
        result.append(name[0])
    return " ".join(result)

def longest(names: list[str]) -> str:
    """Return the longest name. Ties go to the earliest one in the list."""
    # TODO: measure length, do not sort alphabetically. Empty list -> "".
    longest = ""
    for name in names:
        if len(name) > len(longest):
            longest = name
    return longest

if __name__ == "__main__":
    print(f"Signups: {len(SIGNUPS)}")
    print(f"Initials: {initials(SIGNUPS)}")
    print(f"Longest name: {longest(SIGNUPS)}")
    print(f"Running as: {__name__!r}")
