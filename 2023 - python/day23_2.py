
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
from itertools import combinations
import aocd
from collections import deque

longest_path = 0

class Node:
    def __init__(self, pos) -> None:
        self.pos = pos
        self.edges = []
        pass

def find_longest_path(current_node, end_node, path_so_far, steps_so_far):
    global longest_path
    if current_node == end_node:
        if steps_so_far > longest_path:
            print("New longest path: {}".format(steps_so_far))
            longest_path = steps_so_far
            return

    for edge_length, other_node in current_node.edges:
        if other_node in path_so_far:
            # Already visited
            continue

        # Add the weight of the edge and the new node and calculate its longest path
        path_so_far.add(other_node)
        new_steps_so_far = edge_length + 1 + steps_so_far
        find_longest_path(other_node, end_node, path_so_far, new_steps_so_far)
        path_so_far.remove(other_node)

def get_next_node(x, y, all_valid_pos, path_so_far):
    # Walk until a junction
    path_so_far.add((x, y))
    
    while True:
        new_neighbours = get_valid_neighbours(x, y, all_valid_pos, path_so_far)

        if len(new_neighbours) == 1:
            # Only one valid neighbour means not a junction
            path_so_far.add((x, y))
            x, y = new_neighbours[0]
        else:
            # This position is a junction
            edge_length = len(path_so_far) - 1
            neighbouring_node_pos = (x, y)
            return edge_length, neighbouring_node_pos

def get_valid_neighbours(x, y, all_valid_pos, path_so_far = set()):
    return [neigh for neigh in [(x + 1, y), (x -1, y), (x, y + 1), (x, y - 1)] if (neigh in all_valid_pos and not neigh in path_so_far)]

def part_1():
    with open("input.txt") as _file:
        maze = [line.strip() for line in _file]
            

    # positions are (x, y)
    start_pos = (maze[0].find("."), 0)
    end_pos = (maze[-1].find("."), len(maze) - 1)

    all_valid_pos = set(
        [(x, y)
         for x in range(len(maze[0]))
         for y in range(len(maze)) if maze[y][x] == "."
        ]
    )
    
    start_node = Node(start_pos)
    nodes_dict = {start_pos: start_node}
    nodes_to_investigate = deque([start_node])

    while nodes_to_investigate:
        node = nodes_to_investigate.popleft()
        x, y = node.pos
        neighbours = get_valid_neighbours(x, y, all_valid_pos)
        for x_n, y_n in neighbours:
            path_so_far = set([(x, y)])
            edge_length, other_node_pos = get_next_node(x_n, y_n, all_valid_pos, path_so_far)
            node.edges.append((edge_length, other_node_pos))
            if not other_node_pos in nodes_dict.keys() and other_node_pos not in nodes_to_investigate:
                nodes_to_investigate.append(Node(other_node_pos))
        nodes_dict[node.pos] = node

    # Go through all nodes and replace coordinates with links
    for node in nodes_dict.values():
        node.edges = list(map(lambda e: (e[0], nodes_dict[e[1]]), node.edges))
    
    end_node = nodes_dict[end_pos]

    # Once again, go through the graph and recurse at every junction
    find_longest_path(start_node, end_node, set([start_node]), 0)

    # 6499 too high

part_1()