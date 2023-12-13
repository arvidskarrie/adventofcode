
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
import aocd
import re
import math
import collections
import itertools
import functools

USE_TEST_DATA = 0
TEST_DATA = '#...##..#\n#....#..#\n..##..###\n#####.##.\n#####.##.\n..##..###\n#....#..#\n\n#.##..##.\n..#.##.#.\n##......#\n##......#\n..#.##.#.\n..##..##.\n#.#.##.#.'

def sort_into_parts(data: list[str]) -> list[list[str]]:
    return [part.split("\n") for part in "\n".join(data).split("\n\n")]

def get_mirror_plane(part):
    for mirror in range(1, len(part)):
        top_half = part[mirror - 1::-1]
        bottom_half = part[mirror:]

        no_of_errors = sum(
            sum(top_val != bottom_val
                for top_val, bottom_val in zip(top_row, bottom_row))
            for top_row, bottom_row in zip(top_half, bottom_half)
        )

        if no_of_errors == 1:
            return mirror
    return None # if no plane found

def test_vert_and_horiz(part):
    mirror_plane = get_mirror_plane(part)
    if mirror_plane:
        return 100 * mirror_plane

    # rotate the part ccw and do the same thing again
    part = ["".join(row) for row in zip(*part[::-1])]

    mirror_plane = get_mirror_plane(part)
    if mirror_plane:
        return mirror_plane

    assert False, "No pattern found"
    
def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data().splitlines()

    print(sum(test_vert_and_horiz(part) for part in sort_into_parts(input_list)) ) # 32069

part_1()