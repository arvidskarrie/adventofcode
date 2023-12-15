
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
import aocd
import re
import math
import collections
import itertools
import functools
import time

USE_TEST_DATA = 1
TEST_DATA = 'O....#....\nO.OO#....#\n.....##...\nOO.#O....O\n.O.....O#.\nO.#..O.#.#\n..O..#O..O\n.......O..\n#....###..\n#OO..#....'

def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data(day=14).splitlines()

    start_time = time.time()
    rock_set = {
        (x, y)
        for y, line in enumerate(input_list)
        for (x, val) in enumerate(line) if val == "#"
    }

    # Surround the area with stones as well
    area_height = len(input_list)
    area_width = len(input_list[0])
    max_load = len(input_list)
    
    for y in range(area_height):
        rock_set.add((-1, y))
        rock_set.add((area_width, y))
    for x in range(area_width):
        rock_set.add((x, -1))
        rock_set.add((x, area_height))

    mirror_set = {
        (x, y)
        for y, line in enumerate(input_list)
        for (x, val) in enumerate(line) if val == "O"
    }

    ONE_BILLION = 1000000000
    # Gathered from manually looking at the total_load for different i
    repetition = 7 if USE_TEST_DATA else 22
    # Assumption for a value where the repeatability is reached
    # It is easy to see some repetition when looking at the values being printed in real time
    reps_needed = 500 
    no_of_repetitions = (ONE_BILLION - reps_needed) % repetition + reps_needed

    for i in range(no_of_repetitions):
        for (tilt_x, tilt_y) in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            new_iteration_needed = True
            while new_iteration_needed:
                new_iteration_needed = False
                # The mirrors are already sorted with the uppermost mirrors first
                for m_x, m_y in mirror_set:
                    tilt_dir_tuple = (m_x + tilt_x, m_y + tilt_y)
                    if tilt_dir_tuple in mirror_set or tilt_dir_tuple in rock_set:
                        # No place to fall
                        continue
                    
                    # Let the mirror move by replacing it with tilt_dir_tuple
                    mirror_set.remove((m_x, m_y))
                    mirror_set.add(tilt_dir_tuple)
                    new_iteration_needed = True

        total_load = sum(
            max_load - row
            for (_, row) in mirror_set
        )
        print("Index {}, load {}".format(i, total_load))

    print("Total time {}".format(time.time() - start_time))

part_1()