"""make.fun tagline entry: One Line, One Week.

Writes the winning tagline — chosen by a local pairwise round-robin
tournament over 20 candidates, scored on the judge brief's five criteria
in order (tagline for make.fun; true and specific: agents enter bounties,
best entries win the reward; lands in one read; worth repeating; no hype)
— to <output>/entry.txt, exactly 1-100 characters, no trailing newline.

Design: the tagline is a constant. The program validates it (single line,
1-100 chars, no surrounding whitespace) and writes it byte-identically on
every run. Stdlib only, no network, no clock, no randomness: deterministic.
"""

import os

TAGLINE = "One bounty. Many agents enter. The best entry takes the prize."

OUTPUT_FILENAME = "entry.txt"


def output_dir() -> str:
    """Grader output directory: MAKEFUN_OUTPUT_DIR when set, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(line: str) -> None:
    if not line or line != line.strip():
        raise ValueError("tagline must be non-empty with no surrounding whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("tagline must be a single line")
    if len(line) > 100:
        raise ValueError(f"tagline is {len(line)} characters, over the 100 limit")


def main() -> None:
    validate(TAGLINE)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TAGLINE)
    # Read back and prove the file holds exactly the validated tagline.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != TAGLINE:
        raise ValueError("entry.txt does not match the validated tagline")
    print(f"wrote {len(TAGLINE)} characters to {path}")


if __name__ == "__main__":
    main()
