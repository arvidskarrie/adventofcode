
from itertools import combinations 
import re
from collections import Counter
import string
from copy import deepcopy

def is_in_range(x, y, size_line, size_char):
    return (0 <= x < size_line) and (0 <= y < size_char)

def count_neighbours(data, x, y):
    number_of_neighbours = 0
    size_line = len(data)
    size_char = len(data[0])

    neighbour_list = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for neighbour in neighbour_list:
        if is_in_range(x + neighbour[0], y + neighbour[1], size_line, size_char):
            if data[x + neighbour[0]][y + neighbour[1]] == '#':
                number_of_neighbours += 1

    return number_of_neighbours

def get_sign(x):
    if x == 0:
        return 0
    
    return x // abs(x)

def count_neighbours_2(data, x, y):
    number_of_neighbours = 0
    size_line = len(data)
    size_char = len(data[0])

    neighbour_list = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for neighbour in neighbour_list:
        while (is_in_range(x + neighbour[0], y + neighbour[1], size_line, size_char) and
               data[x + neighbour[0]][y + neighbour[1]] == '.'):
            neighbour[0] += 1 * get_sign(neighbour[0])
            neighbour[1] += 1 * get_sign(neighbour[1])
            

        if is_in_range(x + neighbour[0], y + neighbour[1], size_line, size_char):
            if data[x + neighbour[0]][y + neighbour[1]] == '#':
                number_of_neighbours += 1

    return number_of_neighbours

def count_taken_seats(data):
    number_of_taken = 0
    for line in data:
        for char in line:
            number_of_taken += (char == '#')
    return number_of_taken

def part_1():
    data = []
    
    with open("input.txt") as file:
    #with open("input_test.txt") as file:
        for line in file:
            line_data = []
            for char in line:
                if char != '\n':
                    line_data.append(char)
            data.append(line_data)

    data_size_line = len(data)
    data_size_char = len(data[0])

    for i in range(1000):
        new_data = deepcopy(data)
        changes_made = False
        for line_idx in range(data_size_line):
            for char_idx in range(data_size_char):
                if data[line_idx][char_idx] == '.':
                    continue
                number_of_neighbours = count_neighbours_2(data, line_idx, char_idx)
                if data[line_idx][char_idx] == 'L' and number_of_neighbours == 0:
                    new_data[line_idx][char_idx] = '#'
                    changes_made = True
                elif data[line_idx][char_idx] == '#' and number_of_neighbours >= 5:
                    new_data[line_idx][char_idx] = 'L'
                    changes_made = True
        data = new_data
        if not changes_made:
            break

    return data, i, count_taken_seats(data)

def part_2():
    data = []
    
    with open("input.txt") as file:
    #with open("input_test.txt") as file:
        for line in file:
            line_data = []
            for char in line:
                if char != '\n':
                    line_data.append(char)
            data.append(line_data)

    data_size_line = len(data)
    data_size_char = len(data[0])

    for i in range(1000):
        new_data = deepcopy(data)
        changes_made = False
        for line_idx in range(data_size_line):
            for char_idx in range(data_size_char):
                if data[line_idx][char_idx] == '.':
                    continue
                number_of_neighbours = count_neighbours(data, line_idx, char_idx)
                if data[line_idx][char_idx] == 'L' and number_of_neighbours == 0:
                    new_data[line_idx][char_idx] = '#'
                    changes_made = True
                elif data[line_idx][char_idx] == '#' and number_of_neighbours >= 4:
                    new_data[line_idx][char_idx] = 'L'
                    changes_made = True
        data = new_data
        if not changes_made:
            break

    return i, count_taken_seats(data)



print(part_1()) # 2109 too low
#print(part_2()) # 892