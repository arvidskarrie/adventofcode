
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
import aocd
import re
import math
import collections
import itertools
import functools
import time

USE_TEST_DATA = 0
TEST_DATA = '2413432311323\n3215453535623\n3255245654254\n3446585845452\n4546657867536\n1438598798454\n4457876987766\n3637877979653\n4654967986887\n4564679986453\n1224686865563\n2546548887735\n4322674655533'

UNVISITED = False
VISITED = True

RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

STRAIGHT = 4


def get_pos(line, col, limitations: list[int], turn):
    if (line, col) == (0, 0):
        # start position needs special handling since it doesn't have limitations
        if turn == LEFT:
            return (0, 1, RIGHT)
        if turn == RIGHT:
            return (1, 0, DOWN)
        else:
            return (-1, -1, 0)

    old_dir = limitations.index(max(limitations))
    if turn == STRAIGHT:
        dir = old_dir
    if turn == RIGHT:
        dir = (old_dir - 1) % 4
    if turn == LEFT:
        dir = (old_dir + 1) % 4

    if dir == UP:
        line += -1
    if dir == DOWN:
        line += 1
    if dir == LEFT:
        col += -1
    if dir == RIGHT:
        col += 1
    return (line, col, dir)

class Node:
    def __init__(self, line, col, int_value, limitation):
        self.line = line
        self.col = col
        self.int_value = int_value
        self.visited = UNVISITED
        self.distance = 10e6
        self.limitations = limitation

    def get_pos(self):
        return (self.col, self.line)

class Dijkstra:

    def __init__(self, input):

        assert(len(input) == len(input[0])) # Assert square
        self.side_length = len(input)
        
        start_node = Node(0, 0, input[0][0], (0, 0, 0, 0))
        start_node.distance = 0

        self.all_nodes_dict = {(0, 0, (0, 0, 0, 0)): start_node}

        self.unvisited_set = {start_node}

    def run(self, input):
        end_node_pos = (self.side_length - 1, self.side_length - 1)

        while True:
            # for node in self.all_nodes_dict.values():
            #     print(node.get_pos(), node.limitations)
            # Find the unvisited node with smallest tentative path
            sorted_unvisited = list(self.unvisited_set)
            sorted_unvisited.sort(key=lambda n: n.distance)
            current_node = sorted_unvisited[0]
            print(current_node.get_pos()[0] + current_node.get_pos()[1])
            curr_lim = current_node.limitations

            # Since no other path to this node can be shorter, the previously tentative distance will now be definite
            # If end square, we are done.
            col, line = current_node.get_pos()
            if (col, line) == end_node_pos and max(curr_lim) >= 4:
                return current_node.distance

            turning_options = []
            if max(curr_lim) < 10 and (line, col) != (0, 0):
                turning_options.append(STRAIGHT)
            if max(curr_lim) >= 4 or (line, col) == (0, 0):
                turning_options.append(RIGHT)
                turning_options.append(LEFT)
            
            # Go through all its allowed turns
            for turn in turning_options:
                (n_line, n_col, dir) = get_pos(line, col, list(current_node.limitations), turn)
                # If node doesn't exist, skip
                if n_line < 0 or n_col < 0 or n_line >= self.side_length or n_col >= self.side_length:
                    continue

                # if fourth step in same direction, skip
                new_limitation = tuple(curr_lim[i] + 1 if i == dir else 0 for i in range(4))

                if (n_line, n_col, new_limitation) in self.all_nodes_dict.keys():
                    n_node = self.all_nodes_dict[(n_line, n_col, new_limitation)]

                    # If we reach the goal but are unable to stop, skip
                    if (n_col, n_line) == end_node_pos and max(curr_lim) >= 4:
                        continue

                    # If they are already visited, skip
                    if n_node.visited == VISITED:
                        continue
                else:
                    n_node = Node(n_line, n_col, int(input[n_line][n_col]), new_limitation)
                    self.all_nodes_dict[(n_line, n_col, new_limitation)] = n_node
                    self.unvisited_set.add(n_node)

                tentative_dist = current_node.distance + n_node.int_value

                # Only overwrite if a node with lesser limitation does not exist with an equal or lower distance
                n_node.distance = min(n_node.distance, tentative_dist)
                
            
            # Mark current node as visited
            self.unvisited_set.remove(current_node)
            current_node.visited = VISITED


def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        with open("input.txt") as _file:
            input_list = [line.strip() for line in _file]


    # For every square, find the "shortest" way to the end and whatever penalty that gives us in limitations in moves
    dijkstra = Dijkstra(input_list)
    return dijkstra.run(input_list)
    


print(part_1())
