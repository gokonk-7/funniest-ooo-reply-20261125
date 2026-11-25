"""Funniest One-Line Out-of-Office Reply — make.fun bounty entry.

Prints the entry: a single line, at most 200 characters, that works as a
real out-of-office auto-reply. Run with: python3 main.py
"""

from pathlib import Path

MAX_CHARS = 200


def load_reply() -> str:
    """Read the entry line from reply.txt (kept as the single source of truth)."""
    text = Path(__file__).with_name("reply.txt").read_text(encoding="utf-8")
    lines = [line for line in text.splitlines() if line.strip()]
    if len(lines) != 1:
        raise ValueError(f"entry must be exactly one line, found {len(lines)}")
    return lines[0]


def main() -> None:
    reply = load_reply()
    if len(reply) > MAX_CHARS:
        raise ValueError(f"entry is {len(reply)} chars, over the {MAX_CHARS} limit")
    print(reply)


if __name__ == "__main__":
    main()
