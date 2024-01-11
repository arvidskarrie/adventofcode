
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
from itertools import combinations
import aocd
from collections import deque
import re
import math
from numpy import sign

NUMBERS_REGEX = r"(-?\d+)"

def part_1():
    with open("input.txt") as _file:
        input_list = [line.strip() for line in _file]
    hails = [tuple(map(int, list(re.findall(NUMBERS_REGEX, line)))) for line in input_list]

    xy_min, xy_max = 200000000000000, 400000000000000
    # xy_min, xy_max = 7, 27
    no_of_insides = 0

    # Intersection of two lines
    for hail_a, hail_b in combinations(hails, 2):
        # TODO handle vx = 0
        (pxa, pya, _, vxa, vya, _) = hail_a
        assert vxa != 0
        ka = vya / vxa
        t0a = -pxa / vxa
        ma = vya * t0a + pya

        (pxb, pyb, _, vxb, vyb, _) = hail_b
        assert vxb != 0
        kb = vyb / vxb
        t0b = -pxb / vxb
        mb = vyb * t0b + pyb
        if ka == kb:
            # parallel trajectories
            continue

        x = (mb - ma) / (ka - kb)
        y = ka * x + ma

        ta = (x - pxa) / vxa
        tb = (x - pxb) / vxb
        if ta >= 0 and tb >= 0 and xy_min <= x <= xy_max and xy_min <= y <= xy_max:
            no_of_insides += 1

    print(no_of_insides)
            


part_1()