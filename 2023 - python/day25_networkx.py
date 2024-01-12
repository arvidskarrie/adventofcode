
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
from itertools import combinations
import aocd
from collections import deque
import re
import math
from numpy import sign
import sympy as sym
import networkx as nx
import matplotlib.pyplot as plt

def part_1():
    with open("input.txt") as _file:
        input_list = [line.strip() for line in _file]

    G = nx.Graph()
    for line in input_list:
        split_line = line.split(": ")
        head_component = split_line[0]
        connected_components = split_line[1].split(" ")
        for connected in connected_components:
            G.add_edge(head_component, connected)
    

    assert nx.is_connected(G)

    # Use a random component as a basis for a unseparable network
    src = head_component
    first_network_size = 1
    for component in filter(lambda c: c != src, nx.nodes(G)):
        no_of_disjoint_paths = len(list(nx.edge_disjoint_paths(G, src, component)))
        if no_of_disjoint_paths > 3:
            first_network_size += 1
    pass

    print(first_network_size * (len(nx.nodes(G)) - first_network_size))
    nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold')
    plt.show()

part_1()