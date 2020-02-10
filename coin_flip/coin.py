#!/usr/bin/env python

import argparse
import math
import random

parser = argparse.ArgumentParser(description='Flip some coins.')
parser.add_argument('flips', metavar='N', type=int, nargs="+",
help='number of coins to flip.')
args = parser.parse_args()
init_counts = {"heads": 0, "tails": 0}

def flip(args, counts):
    for _ in range(args.flips[0]):
        choice = random.choice(["heads", "tails"])
        counts[choice] += 1
    return counts

counts = flip(args, init_counts)
print(counts["heads"], "heads")
print(counts["tails"], "tails")
print("delta: ", abs(counts["heads"] - counts["tails"]))

