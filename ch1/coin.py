#!/usr/bin/env python

import argparse
import math
import random
from typing import Dict


def flip(flips: int) -> Dict[str, int]:
    counts = {"heads": 0, "tails": 0}
    for _ in range(flips):
        choice = random.choice(["heads", "tails"])
        counts[choice] += 1
    return counts


def main() -> None:
    parser = argparse.ArgumentParser(description="Flip some coins.")
    parser.add_argument(
        "flips",
        metavar="N",
        type=int,
        nargs="+",
        help="number of coins to flip.",
    )
    args = parser.parse_args()

    counts = flip(args.flips[0])
    for count in counts:
        print(counts[count], count)
    print("delta: ", abs(counts["heads"] - counts["tails"]))


if __name__ == "__main__":
    main()
