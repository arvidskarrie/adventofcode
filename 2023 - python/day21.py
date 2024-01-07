
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
from numpy import polyfit

# NO_OF_STEPS = 1000
NO_OF_STEPS = 26501365

def find_start_pos(input):
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == "S":
                return (x, y) # TODO clean

def quadratic_equation_and_value(x_coords, y_coords, final_x):
    """
    Fits a quadratic equation to three points and evaluates the equation at a given x-coordinate.

    :param x_coords: List of three x-coordinates.
    :param y_coords: List of three y-coordinates.
    :param final_x: The x-coordinate at which to evaluate the fitted quadratic equation.
    :return: Coefficients of the quadratic equation and the function value at final_x.
    """
    # Fit a quadratic equation (2nd degree polynomial) to the points
    coefficients = polyfit(x_coords, y_coords, 2)

    # The quadratic equation is of the form ax^2 + bx + c
    a, b, c = coefficients

    # Evaluate the quadratic equation at final_x
    next_x = x_coords[-1] + 262
    next_y = a * next_x**2 + b * next_x + c
    print("Next y guess: {}".format(next_y))

    # Evaluate the quadratic equation at final_x
    final_y = a * final_x**2 + b * final_x + c
    print("{} x^2 + {} x + {}".format(a, b, c))
    print("final y = {}".format(final_y))

    # return coefficients, final_y

def run_bfs(input):

    assert(len(input) == len(input[0])) # Assert square
    side_length = len(input) # 131
    double_side_length = 2 * side_length
    
    def get_index(s):
        start_steps_value = NO_OF_STEPS % double_side_length
        return (s + double_side_length - start_steps_value - 1) // double_side_length

    
    start_col, start_row = find_start_pos(input)

    seen_set = {(start_col, start_row)}
    node_queue = deque([(start_col, start_row, 0)])
    no_of_even_squares = {}
    x_values = []
    y_values = []

    while node_queue:
        # BFS means choosing the "eldest" node, which will automatically have the shortest path.
        col, line, steps_taken = node_queue.popleft()

        # if it is an even number of steps remaining, it is a solution
        if steps_taken % 2 == 1:
            index = get_index(steps_taken)
            if not index in no_of_even_squares.keys():
                print("Finishing entry: At {} steps: {}".format(
                    steps_taken - 2,
                    sum(no_of_even_squares.values())
                ))
                x_values.append(steps_taken - 2)
                y_values.append(sum(no_of_even_squares.values()))
                if len(x_values) >= 6:
                    quadratic_equation_and_value(
                        x_values[-6:],
                        y_values[-6:],
                        NO_OF_STEPS)
                # print("New index {} at {}".format(index, steps_taken))
                no_of_even_squares[index] = 1
            else:
                no_of_even_squares[index] += 1

        # If there are no steps remaining, we are done

        if steps_taken == NO_OF_STEPS: 
            continue

        # Go through all its neighbours
        neighbour_list = [(col, line+1), (col, line-1), (col+1, line), (col-1, line)]
        for (n_col, n_line) in neighbour_list:
            # If the neighbour is already visited, no need to add it again
            if (n_col, n_line) in seen_set:
                continue

            # Do not walk through rocks
            if input[n_line % side_length][n_col % side_length] == "#":
                continue

            # This square is now seen, with one step less than before
            # No other path here may be shorter
            seen_set.add((n_col, n_line))

            # We also need to investigate the neighbours of this node
            node_queue.append((n_col, n_line, steps_taken + 1))

    print("Total number of even nodes {}".format(sum(no_of_even_squares.values())))

    return sum(no_of_even_squares.values())
                

def part_1():
    with open("input.txt") as _file:
        input_list = [line.strip() for line in _file]

    # For every square, find the "shortest" way to the end and whatever penalty that gives us in limitations in moves
    return run_bfs(input_list)
    


print(part_1())

# 607334325965753 too high