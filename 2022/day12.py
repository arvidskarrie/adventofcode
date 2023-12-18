
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations
import aocd
import re

USE_TEST_DATA = 0
TEST_DATA = 'Sabqponm\nabcryxxl\naccszExk\nacctuvwj\nabdefghi'

UNVISITED = False
VISITED = True

RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
else:
    input_list = aocd.get_data(day=12).splitlines()

class Node:
    def __init__(self, line, col, ord_value):
        self.line = line
        self.col = col
        self.ord_value = ord_value
        self.visited = UNVISITED
        self.distance = 1000

class Dijkstra:

    def __init__(self, input, part):
        self.no_lines = len(input)
        self.no_columns = len(input[0])
        self.nodes = []
        self.unvisited_set = set()

        # Initiate nodes
        for i in range(self.no_lines):
            node_line = []
            for j in range(self.no_columns):
                if input[i][j] == ord('S') or (input[i][j] == ord('a') and part == 2):
                    # Set start node
                    node = Node(i, j, ord('a'))
                    node.distance = 0
                elif input[i][j] == ord('E'):
                    node = Node(i, j, ord('z'))
                    self.end_node = node
                else:
                    node = Node(i, j, input[i][j])

                node_line.append(node)
                self.unvisited_set.add(node)
            self.nodes.append(node_line)

    def print_distances(self):
        for i in range(self.no_lines):
            dist_line = []
            for j in range(self.no_columns):
                dist_line.append(self.nodes[i][j].distance)
            print(dist_line)
        print()

    def run(self):

        while True:
            # Find the unvisited node with smallest tentative path
            lowest_distance = 999
            for node in self.unvisited_set:
                if node.distance < lowest_distance:
                    c_node = node
                    lowest_distance = node.distance

            # If it is our goal, nothing more to do
            if c_node == self.end_node:
                return c_node.distance

            # For the current node
            line = c_node.line
            col = c_node.col
            # print('new lowest', line, col, lowest_distance)

            # neighbour_list = [(line, col+1), (line, col-1), (line+1, col), (line-1, col)]s
            neighbour_list = [(line, col+1, RIGHT), (line, col-1, LEFT), (line+1, col, DOWN), (line-1, col, UP)]

            # Go through all its neighbours
            for (n_line, n_col, dir) in neighbour_list:
                # If node doesn't exist, skip
                if n_line < 0 or n_col < 0 or n_line >= self.no_lines or n_col >= self.no_columns:
                    continue

                # if fourth step in same direction, skip
                new_limitation = (0 for _ in range(4))
                new_limitation[dir] = current_node.limitations[dir] + 1
                                  
                n_node = self.nodes[n_line][n_col]

                # If they are already visited, skip
                if n_node.visited == VISITED:
                    continue
                
                # If no connection possible
                if (n_node.ord_value - c_node.ord_value) > 1:
                    continue

                # If lower than their current value, replace
                if c_node.distance + 1 < n_node.distance:
                    n_node.distance = c_node.distance + 1

            # Mark current node as visited
            self.unvisited_set.remove(c_node)
            c_node.visited = VISITED


def part_1(part):
    ord_input = [[ord(s) for s in xs] for xs in input_list]
    
    dijkstra = Dijkstra(ord_input, part)

    return dijkstra.run()




print(part_1(1))
print(part_1(2))
