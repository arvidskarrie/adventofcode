
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
    return [
        part.split("\n")
        for part in "\n".join(data).split("\n\n")
    ]

def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data().splitlines()

    parts = sort_into_parts(input_list)

    pattern_sum = 0

    for part in parts:
        # Test horizontal symmetry
        for mirror in range(1, len(part)):
            number_of_tests = min(mirror, len(part) - mirror)
            if all([
                part[mirror - 1 - i] == part[mirror + i]
                for i in range(number_of_tests)
            ]):
                pattern_sum += 100 * mirror
                break
        else:
            # if break has not occured
            # rotate the part ccw and do the same thing again
            y_max = len(part)
            x_max = len(part[0])
            part = [[ \
                part[x][y] for x in range(y_max)[::-1] \
                ] for y in range(x_max) \
            ]

            # Test vertical symmetry
            for mirror in range(1, len(part)):
                number_of_tests = min(mirror, len(part) - mirror)
                if all([
                    part[mirror - 1 - i] == part[mirror + i]
                    for i in range(number_of_tests)
                ]):
                    pattern_sum += mirror
                    break
            else:
                # No mirror found
                assert False
    
    print(pattern_sum) # 31746 too low

part_1()