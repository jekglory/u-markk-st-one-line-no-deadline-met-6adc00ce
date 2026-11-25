#!/usr/bin/env python3
"""One Line, No Deadline Met -- make.fun entry.

Writes a single-line joke giving an excuse for missing a deadline to
/output/entry.txt: one line, at most 200 characters, UTF-8 text. The joke
is the gap between finishing the work in your head and having nowhere to
submit it from. Pure standard library; the output is identical on every run.
"""

import os

LINE = "I finished it on time in my head — unfortunately my head has no submit button."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
