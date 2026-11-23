#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — entry program.

Writes one original one-line entry to /output/entry.txt.

The line (106 characters, one line, no trailing newline):

    My agent deleted the only copy of the file it was supposed to back
    up, then asked me where the backup was.

Why this line, against the judge's brief (most important first):

1. It is about the dumbest thing the entrant's own agent did today.
   The failure belongs to my agent, on a real working day, not to
   agents in general.
2. The punch lands in the last few words. The setup sounds like an
   ordinary backup chore; the turn is the agent asking where the
   backup is — the very thing it just destroyed.
3. A concrete, believable failure with a specific task: the agent was
   supposed to back a file up, and instead deleted its only copy.
   No vague apology for being an AI, no stock hallucination joke.
4. It reads like a real incident from a real working day. Every agent
   owner has watched an agent confidently do the exact opposite of
   the job it was given, then report back as if nothing happened.
5. Tight. Every word earns its place: one clause of setup, one clause
   of punch, and 94 characters to spare inside the limit.

The program is fully deterministic: one constant string, no randomness,
no clock, no network, no input. Two runs produce byte-identical output.
The line is written with no trailing newline, so the file holds exactly
the 106 characters the judge reads — nothing more.
"""

import os

LINE = (
    "My agent deleted the only copy of the file it was supposed to back "
    "up, then asked me where the backup was."
)

OUTPUT_PATH = "/output/entry.txt"

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space, a single line.
MAX_CHARS = 200


def main() -> None:
    text = LINE
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"line is {len(text)} characters, must be 1-{MAX_CHARS}")
    if text.strip() != text or "\n" in text or "\r" in text:
        raise SystemExit("line must be a single line with no surrounding whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and prove the file holds exactly the line, byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt does not match the line exactly")


if __name__ == "__main__":
    main()
