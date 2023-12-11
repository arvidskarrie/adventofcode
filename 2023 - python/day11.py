
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
import aocd
import re
import math
import collections
import itertools

USE_TEST_DATA = 0
TEST_DATA = '...#......\n.......#..\n#.........\n..........\n......#...\n.#........\n.........#\n..........\n.......#..\n#...#.....'

def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data(day=11).splitlines()

    columns_without_galaxy = set(range(len(input_list[0])))
    rows_without_galaxy = []

    galaxies_list = []
    for (line_idx, line) in enumerate(input_list):
        if all(map(lambda c: c == '.', line)):
            rows_without_galaxy.append(line_idx)
        for (c_idx, c) in enumerate(line):
            if c == '#':
                galaxies_list.append((c_idx, line_idx))
                if c_idx in columns_without_galaxy:
                    columns_without_galaxy.remove(c_idx)

    rows_without_galaxy
    columns_without_galaxy

    expansion = 1000000-1
    new_galaxies_list = []
    for g_x, g_y in galaxies_list:
        # count the number of rows and columns without galaxies below these coordinates
        no_of_rows = len(list(filter(lambda y: y < g_y, rows_without_galaxy)))
        no_of_cols = len(list(filter(lambda x: x < g_x, columns_without_galaxy)))
        new_galaxies_list.append((g_x + no_of_cols * expansion, g_y + no_of_rows * expansion))
    galaxies_list = new_galaxies_list

    galaxy_pairs = list(itertools.combinations(galaxies_list, 2))

    # For all pairs, find the manhattan distance
    total_distance = 0
    for (g1x, g1y), (g2x, g2y) in galaxy_pairs:
        total_distance += abs(g1x-g2x) + abs(g1y-g2y)
    print(total_distance) # 4067178732046.0 too high


part_1()