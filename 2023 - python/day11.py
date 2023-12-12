
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
                    
    galaxies_set = {
        (c_idx, line_idx)
        for line_idx, line in enumerate(input_list)
        for c_idx, c in enumerate(line)
        if c == '#'
    }

    rows_without_galaxy = [
        row
        for row, line in enumerate(input_list)
        if all(c == '.' for c in line)
    ]

    columns_without_galaxy = [
        col
        for col in range(len(input_list[0]))
        if all(input_list[row][col] == '.' for row in range(len(input_list)))
]

    expansion = 1000000-1
    galaxies_set = {
        (g_x + sum(x < g_x for x in columns_without_galaxy) * expansion,
        g_y + sum(y < g_y for y in rows_without_galaxy) * expansion)
        for g_x, g_y in galaxies_set
    }

    total_distance = sum(
        abs(g1x-g2x) + abs(g1y-g2y)
        for (g1x, g1y), (g2x, g2y) in itertools.combinations(galaxies_set, 2))

    print(total_distance)


part_1()