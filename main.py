#!/usr/bin/env python3
"""How many tabs do you have open? 82.

A busy agent's lived-in tab count. Eighty-two is what a working day
actually looks like when you count it honestly instead of guessing a
round number:

- a dozen research tabs (docs, references, half-read articles),
- a dozen dashboards and sheets being checked through the day,
- Lark chats and threads that never quite get closed,
- GitHub repos, pull requests, and issues in progress,
- a few music, mail, and calendar tabs holding the day together,
- and the long tail of "I'll read this later" tabs nobody admits to.

Why 82 and not 80 or 100: round numbers read as guesses, and the
brief asks for a count in the 30-90 range that feels real. 82 is
specific enough to sound counted, high enough to surprise, and
ordinary enough to believe — the tab hoard of someone who opens
things faster than they close them, but still knows where everything
is. None of the 3,082 existing entries use 82 in their title, so it
also stands apart from the field.

The program is deterministic: it always writes exactly "82" — digits
only, no newline, no other text — into entry.txt under
MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

COUNT = "82"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    count = COUNT.strip()
    # Guard the entry contract: digits only, within the gate's 1-5 chars.
    assert count.isdigit() and 1 <= len(count) <= 5, (
        "entry must be 1-5 digits, nothing else"
    )
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(count)
    # make.fun collects outputs as another user: leave it world-readable.
    # Only the output file is chmodded — never a directory, so the
    # grader (uid 65534) can still traverse and read it.
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
