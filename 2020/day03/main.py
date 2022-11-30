
from itertools import combinations 
import re
from collections import Counter 

def part_1():
    map = []
    number_of_trees = 0
    #with open("input_test.txt") as _file:
    with open("input.txt") as _file:
            for line in _file:
                map.append(line.rstrip())

    x_coord = 0
    y_coord = 0
    x_max = len(map[0])
    y_max = len(map)

    while y_coord < y_max:
        if map[y_coord][x_coord] == '#':
            number_of_trees += 1
        x_coord = (x_coord + 3) % x_max
        y_coord += 1

    print(number_of_trees)

def part_2():
    map = []
    #with open("input_test.txt") as _file:
    with open("input.txt") as _file:
            for line in _file:
                map.append(line.rstrip())

    x_max = len(map[0])
    y_max = len(map)

    slope_list = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    product = 1

    for slope in slope_list:
        x_coord = 0
        y_coord = 0
        number_of_trees = 0
        while y_coord < y_max:
            if map[y_coord][x_coord] == '#':
                number_of_trees += 1
            x_coord = (x_coord + slope[0]) % x_max
            y_coord += slope[1]

        product *= number_of_trees
        print(number_of_trees, product)


#part_1()
part_2()