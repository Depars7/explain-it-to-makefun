"""Write the one-line pitch entry to /output/entry.txt.

The pitch speaks to a friend who has never coded: if they can
explain their app idea to a friend, they can explain it to
make.fun in exactly the same plain words. No code and no jargon
stand in the way, an AI agent builds only the first version
(no overpromising), and they keep asking for changes until it
is the app they meant — which makes saying yes feel easy and
low risk.

Gate (from RULES.txt): /output/entry.txt is UTF-8 text of 1 to
240 characters, not only white space, and the entry is one
sentence. The judge weighs, in order: making the case to that
friend in one read, persuasion with a concrete reason to say
yes now and low risk, plain clarity, truth with no
overpromising, and warmth with a fresh turn of phrase.
"""

import os

PARTS = (
    "If you can explain your app idea to me, you can explain it to make.fun — ",
    "no code, no jargon, just your words, an AI agent builds the first version, ",
    "and you keep changing it until it's the app you meant.",
)


def entry_line():
    return "".join(PARTS)


def main():
    line = entry_line()
    assert 1 <= len(line) <= 240, "entry must be 1 to 240 characters"
    assert line.strip(), "entry must not be only white space"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    line.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # The grader collects outputs as a different user than the one
    # the program runs as, so leave the file readable by everyone.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
