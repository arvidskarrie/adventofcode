
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

class Node:
    def __init__(self, pos):
        (self.col, self.line) = pos
        self.visited = UNVISITED
        self.distance = 10e6

    def get_pos(self): # x y
        return (self.col, self.line)

def find_start_pos(input):
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == "S":
                return (x, y) # TODO clean

class Dijkstra:
    def __init__(self, input):

        assert(len(input) == len(input[0])) # Assert square
        self.side_length = len(input)
        
        start_pos = find_start_pos(input)
        start_node = Node(start_pos)
        start_node.distance = 0

        self.all_nodes_dict = {start_pos: start_node}
        self.unvisited_set = set([start_node])
        pass
    # def print_distances(self):
    #     for i in range(self.no_lines):
    #         dist_line = []
    #         for j in range(self.no_columns):
    #             if i in self.nodes.keys() and j in 
    #             dist_line.append(self.nodes[i][j].distance)
    #         print(dist_line)
    #     print()

    def print_path(self, input: list[str]):
        copied_input = input[:]
        for (x, y) in self.all_nodes_dict.keys():
            copied_input[y] = copied_input[y][:x] + "O" + copied_input[y][x+1:]
        for (x, y) in [node.get_pos() for node in self.unvisited_set]:
            copied_input[y] = copied_input[y][:x] + "u" + copied_input[y][x+1:]

        for copied_line in copied_input:
            print(copied_line)
        print()

    def calculate_no_of_possible_squares(self, steps):
        no_of_squares = 0
        for node in self.all_nodes_dict.values():
            if node in self.unvisited_set:
                continue
            elif node.distance > steps or node.distance % 2 != steps % 2:
                continue
            else:
                no_of_squares += 1
        return no_of_squares

    def run(self, input):
        while True:
            # self.print_path(input)
            # Find the unvisited node with smallest tentative path
            sorted_unvisited = list(self.unvisited_set)
            sorted_unvisited.sort(key=lambda n: n.distance)
            current_node = sorted_unvisited[0]

            # Since no other path to this node can be shorter,
            # the previously tentative distance will now be definitive.
            # If distance is greater than 64, we are done

            if current_node.distance > 64: #
                return self.calculate_no_of_possible_squares(64)

            col, line = current_node.get_pos()
            neighbour_list = [(col, line+1), (col, line-1), (col+1, line), (col-1, line)]
            # Go through all its neighbours
            for (n_col, n_line) in neighbour_list:
                # If out of bounds, skip
                if n_line < 0 or n_col < 0 or n_line >= self.side_length or n_col >= self.side_length:
                    continue

                if (n_col, n_line) in self.all_nodes_dict.keys():
                    n_node = self.all_nodes_dict[(n_col, n_line)]

                    # If they are already visited, skip
                    if n_node.visited == VISITED:
                        continue
                elif input[n_line][n_col] == "#":
                    # Do not walk through rocks
                    continue
                else:
                    n_node = Node((n_col, n_line))
                    self.all_nodes_dict[(n_col, n_line)] = n_node
                    self.unvisited_set.add(n_node)

                tentative_dist = current_node.distance + 1

                # Only overwrite if a node with lesser limitation does not exist with an equal or lower distance
                n_node.distance = min(n_node.distance, tentative_dist)
                
            
            # Mark current node as visited
            self.unvisited_set.remove(current_node)
            current_node.visited = VISITED
            print(current_node.distance, len(self.all_nodes_dict) - len(self.unvisited_set) - 1)
            pass



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
