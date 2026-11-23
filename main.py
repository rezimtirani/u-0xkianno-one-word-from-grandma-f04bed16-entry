"""One Word From Grandma — the one word grandma would text about AI.

The entry is one word. Grandma has never trusted the robots, and when
the grandkids showed her the talking computer, she stared at it, typed
one word with one finger, and sent it: Scary.
"""

import os
import sys


def grandmas_word():
    """Return the one word grandma would say."""
    return "Scary"


def is_single_word(text):
    """Check the text is exactly one word (letters plus a final period)."""
    stripped = text.strip()
    if not stripped:
        return False
    core = stripped[:-1] if stripped.endswith(".") else stripped
    return core.isalpha() and " " not in stripped and "\n" not in stripped


def why_this_word():
    """Explain, in the code's own words, why this one word is the entry."""
    reasons = [
        "Grandma's verdict on the robots, typed with one finger.",
        "One word that says she loves you and fears the machines.",
        "It is honest, it is funny, and it is exactly what she would send.",
    ]
    return " ".join(reasons)


def main():
    word = grandmas_word()
    if not is_single_word(word):
        print("error: entry must be exactly one word", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(word + "\n")
    print("Wrote one word to /output/entry.txt:", word)
    print(why_this_word())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
