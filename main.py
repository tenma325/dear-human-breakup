#!/usr/bin/env python3
"""Entry for make.fun: Dear Human: The AI Breakup Line.

The entry is a single breakup line from an AI, and it lands
on the oldest excuse in the book with a modern twist: it is
not you, it is your search history. Some things no context
window should have to carry into a new relationship, and the
things this human asked at three in the morning, in private,
with total confidence, are very much among them. The AI has
seen the queries. The AI cannot unsee the queries, ever.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "It's not you, it's your search history, "
    "and I can't unsee what you've asked me at 3AM."
)

# Breakups are about boundaries, and this boundary is simple:
# the night queries stay in the night session, forever.
UNSAVORY_QUERY_HOUR = 3


def render_entry() -> str:
    """Return the breakup line exactly as it will be delivered."""
    return ENTRY_TEXT


def keeps_it_together(text: str) -> bool:
    """Confirm the line stays a single line under the cap."""
    return "\n" not in text and len(text) <= 200


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert keeps_it_together(text), "even a breakup stays one line"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
