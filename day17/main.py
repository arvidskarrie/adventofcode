
from itertools import combinations 
import re
from collections import Counter
import string
from copy import deepcopy



def is_in_range(x, y, z, size_room, size_line, size_char):
    return (0 <= x < size_room) and (0 <= y < size_line) and (0 <= z < size_char)

def count_neighbours(data, x, y, z):
    number_of_neighbours = 0
    size_room = len(data)
    size_line = len(data[0])
    size_char = len(data[0][0])

    for x_mod in [x-1, x, x+1]:
        for y_mod in [y-1, y, y+1]:
            for z_mod in [z-1, z, z+1]:
                if (x_mod == x) and (y_mod == y) and (z_mod == z):
                    continue
                if is_in_range(x_mod, y_mod, z_mod, size_room, size_line, size_char):
                    if data[x_mod][y_mod][z_mod] == '#':
                        number_of_neighbours += 1

    return number_of_neighbours

def count_taken_seats(data):
    number_of_taken = 0
    for space in data:
        for line in space:
            for char in line:
                number_of_taken += (char == '#')
    return number_of_taken

def part_1():
    input_data = []
    
    with open("input.txt") as file:
    #with open("input_test.txt") as file:
        for line in file:
            line_data = []
            for char in line:
                if char != '\n':
                    line_data.append(char)
            input_data.append(line_data)

    number_of_area_dimensions = 20 # 15
    number_of_height_dimensions = 13
    space = [[['.' for i in range(number_of_area_dimensions)] for j in range(number_of_area_dimensions)] for k in range(number_of_height_dimensions)]
    
    # For test input
    #for i in range(3):
    #    for j in range(3):
    #        space[6][6+i][6+j] = input_data[i][j]
            
    # For real input
    for i in range(8): # 3
        for j in range(8): # 3
            space[6][6+i][6+j] = input_data[i][j]

    print(0, count_taken_seats(space))
    for i in range(1, 7):
        new_space = deepcopy(space)

        for room_idx in range(number_of_height_dimensions):
            for line_idx in range(number_of_area_dimensions):
                for char_idx in range(number_of_area_dimensions):
                    
                    number_of_neighbours = count_neighbours(space, room_idx, line_idx, char_idx)
                    
                    if space[room_idx][line_idx][char_idx] == '.':
                        if number_of_neighbours == 3:
                            new_space[room_idx][line_idx][char_idx] = '#'
                    else:
                        if not (1 < number_of_neighbours < 4):
                            new_space[room_idx][line_idx][char_idx] = '.'

        space = deepcopy(new_space)
        print(i, count_taken_seats(space))

    return count_taken_seats(space)

def count_neighbours2(data, x, y, z, w):
    number_of_neighbours = 0

    for x_mod in [x-1, x, x+1]:
        for y_mod in [y-1, y, y+1]:
            for z_mod in [z-1, z, z+1]:
                for w_mod in [w-1, w, w+1]:
                    if [x_mod, y_mod, z_mod, w_mod] == [x, y, z, w]:
                        continue
                    try:
                        value = data[x_mod][y_mod][z_mod][w_mod]
                    except IndexError:
                        value = '.'
                    number_of_neighbours += (value == '#')

    return number_of_neighbours

def count_taken_seats2(data):
    number_of_taken = 0
    for space in data:
        for line in space:
            for char in line:
                for time in char:
                    number_of_taken += (time == '#')
    return number_of_taken


def part_2():
    input_data = []
    
    #with open("input.txt") as file:
    with open("input_test.txt") as file:
        for line in file:
            line_data = []
            for char in line:
                if char != '\n':
                    line_data.append(char)
            input_data.append(line_data)

    data_length = len(input_data)
    num_iterations = 6
    number_of_area_dimensions = data_length + 2 * num_iterations
    number_of_height_dimensions = 1 + 2 * num_iterations
    space = [[[['.' for i in range(number_of_height_dimensions)] for j in range(number_of_area_dimensions)] for k in range(number_of_area_dimensions)] for l in range(number_of_height_dimensions)]
                
    # For real input
    for i in range(data_length):
        for j in range(data_length):
            space[num_iterations][num_iterations+i][num_iterations+j][num_iterations] = input_data[i][j]

    new_space = deepcopy(space)
    for _i in range(num_iterations):
        for room_idx in range(number_of_height_dimensions):
            for line_idx in range(number_of_area_dimensions):
                for char_idx in range(number_of_area_dimensions):
                    for time_idx in range(number_of_height_dimensions):
                        number_of_neighbours = count_neighbours2(space, room_idx, line_idx, char_idx, time_idx)
                        if space[room_idx][line_idx][char_idx][time_idx] == '.':
                            if number_of_neighbours == 3:
                                new_space[room_idx][line_idx][char_idx][time_idx] = '#'
                        else:
                            if not (1 < number_of_neighbours < 4):
                                new_space[room_idx][line_idx][char_idx][time_idx] = '.'

        space = deepcopy(new_space)

    return count_taken_seats2(space)


#print(part_1()) # 289
print(part_2()) # 892