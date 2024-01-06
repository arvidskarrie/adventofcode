
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
import aocd
import re
import math
import collections
import itertools
import functools
import time
from collections import deque

def find_start_pos(input):
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == "S":
                return (x, y) # TODO clean

def run_bfs(input):

    assert(len(input) == len(input[0])) # Assert square
    side_length = len(input)
    
    start_col, start_row = find_start_pos(input)

    seen_set = {(start_col, start_row)}
    node_queue = deque([(start_col, start_row, 64)])
    no_of_even_squares = 0

    while node_queue:
        # BFS means choosing the "eldest" node, which will automatically have the shortest path.
        col, line, remaining_steps = node_queue.popleft()

        # if it is an even number of steps remaining, it is a solution
        no_of_even_squares += remaining_steps % 2 == 0

        # If there are no steps remaining, we are done
        if remaining_steps == 0: 
            continue

        # Go through all its neighbours
        neighbour_list = [(col, line+1), (col, line-1), (col+1, line), (col-1, line)]
        for (n_col, n_line) in neighbour_list:
            # If out of bounds, skip
            if n_line < 0 or n_col < 0 or n_line >= side_length or n_col >= side_length:
                continue

            # If the neighbour is already visited, no need to add it again
            if (n_col, n_line) in seen_set:
                continue

            # Do not walk through rocks
            if input[n_line][n_col] == "#":
                continue

            # This square is now seen, with one step less than before
            # No other path here may be shorter
            seen_set.add((n_col, n_line))

            # We also need to investigate the neighbours of this node
            node_queue.append((n_col, n_line, remaining_steps - 1))

    return no_of_even_squares
                

def part_1():
    with open("input.txt") as _file:
        input_list = [line.strip() for line in _file]

    # For every square, find the "shortest" way to the end and whatever penalty that gives us in limitations in moves
    return run_bfs(input_list)
    


print(part_1() == 3651)
