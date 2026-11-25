"""Entry for "Have You Tried Turning It Off?" (make.fun).

A hopeless tech support agent answers a desperate customer with the
one line every caller dreads hearing, then makes the wait itself the
punchline: the fix is trivial, the ticket queue is not.
"""

ENTRY = (
    "Have you tried turning it off and on again? Great — now do it "
    "a third time, slower, while I pretend the ticket system isn't "
    "also frozen."
)


def get_entry() -> str:
    """Return the entry line."""
    return ENTRY


def write_entry(output_dir: str) -> str:
    """Write the entry to entry.txt inside output_dir and return its path."""
    import os

    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(get_entry())
    return path


def main() -> None:
    """Write the entry to $MAKEFUN_OUTPUT_DIR (default /output)."""
    import os

    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
