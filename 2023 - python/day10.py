
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
import aocd
import re
import math
import collections
import itertools

USE_TEST_DATA = 0
TEST_DATA = '..........\n.S------7.\n.|F----7|.\n.||OOOO||.\n.||OOOO||.\n.|L-7F-J|.\n.|II||II|.\n.L--JL--J.\n..........'



def get_neighbours(this_coord: (int, int), full_input):
    (x, y) = this_coord
    this_char = full_input[y][x]

    if this_char == "S":
        # We only need one starting point
        # For line counting measures, we need to find if the starting point has a
        # connection upwards
        if full_input[y - 1][x] in ["|", "F", "7"]:
            full_input[y][x] = "|"
            return [(x - 1, y)]
        if full_input[y][x + 1] in ["-", "7", "J"]:
            return [(x + 1, y)]
        assert full_input[y + 1][x] in ["|", "F", "7"]
        return [(x, y + 1)]

    if this_char == "|":
        return [(x, y - 1), (x, y + 1)]
    if this_char == "-":
        return [(x - 1, y), (x + 1, y)]
    if this_char == "F":
        return [(x + 1, y), (x, y + 1)]
    if this_char == "J":
        return [(x - 1, y), (x, y - 1)]
    if this_char == "7":
        return [(x, y + 1), (x - 1, y)]
    if this_char == "L":
        return [(x, y - 1), (x + 1, y)]

def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data(day=10).splitlines()


    # Find the start position and the two connected pipes
    for (y_idx, line) in enumerate(input_list):
        if 'S' in line:
            start_position = (line.find('S'), y_idx)
            break
    
    loop_list = [start_position]
    # Iterate over the current loop list and add one item every time
    loop_idx = 0
    while 0 <= loop_idx < len(loop_list):
        current_pos = loop_list[loop_idx]
        new_positions = get_neighbours(current_pos, input_list)
        for pos in new_positions:
            if not pos in loop_list:
                loop_list.append(pos)
        # If no position is added, the loop will always stop
        loop_idx += 1

    print(loop_list)
    print("Half loop length = {}".format(len(loop_list) / 2))

    # Finding whether a position is inside or outside the loop, we can
    # count the number of lines between it and infinity.
    # If an odd number, it is inside, otherwise outside.
    # Assuming a coord is defined by its upper side and infinity is defined as
    # first char in the line, we can count the number of times we pass the loop line

    no_of_enclosed = 0
    for (y, line) in enumerate(input_list):
        is_inside_loop = False
        for (x, c) in enumerate(line):
            if (x, y) not in loop_list:
                no_of_enclosed += 1 if is_inside_loop else 0
            elif c in ["|", "L", "J"]:
                # The upper half will switch on |, L or J 
                is_inside_loop =  not is_inside_loop

        assert not is_inside_loop
    
    print(no_of_enclosed)



part_1()