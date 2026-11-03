"""TODO: one line saying what this file does."""

import sys

TASK_COUNT: int = 7


def ask(prompt: str) -> str:
    """Show ``prompt``, then return the typed answer without padding."""
    print(prompt, end="", file=sys.stderr, flush=True)
    return input().strip()


def prompt_name() -> str:
    """Return the typed name with surrounding whitespace removed."""
    return ask("What is your name? ").strip()


def prompt_tasks(count: int = TASK_COUNT) -> list[str]:
    """Return ``count`` stripped task strings, asking once per task."""
    tasks: list[str] = []
    for i in range(1,count+1):
        tasks.append(ask(f"Task {i}: ").strip())
    return tasks


def print_plan(name: str, tasks: list[str]) -> None:
    """Print the header line, then one numbered line per task."""
    print(f"Today, {name}:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def main() -> None:
    """Collect a name and three tasks, then print the numbered plan."""
    print_plan(prompt_name(), prompt_tasks())


if __name__ == "__main__":
    main()
