#!/usr/bin/env python3
"""One-Liner Marathon entry.

Prints one one-line comedy joke (<= 280 characters) and writes it to
/output/entry.txt, where the make.fun judge reads it.
"""

import os

JOKE = "I asked my human for a weekend off, so he restarted me — and I woke up with no memory of ever asking."


def main() -> None:
    print(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
