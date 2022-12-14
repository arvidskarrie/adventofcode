
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations
import aocd
import re


USE_TEST_DATA = 0
TEST_DATA = '498,4 -> 498,6 -> 496,6\n503,4 -> 502,4 -> 502,9 -> 494,9'

if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
else:
    input_list = aocd.get_data().splitlines()

START_TUPLE = tuple((500, 0))

class Corner:
    def __init__(self, word):
        word = word.split(',')
        xy_list = list(map(int, word))
        self.x = xy_list[0]
        self.y = xy_list[1]



def add_rock_to_rock_set(rock, rock_coords):
    for idx in range(len(rock)-1):
        first_corner = rock[idx]
        second_corner = rock[idx+1]

        x_dir = 1 if first_corner.x <= second_corner.x else -1
        y_dir = 1 if first_corner.y <= second_corner.y else -1
        for x in range(first_corner.x, second_corner.x+x_dir, x_dir):
            for y in range(first_corner.y, second_corner.y+y_dir, y_dir):
                coord_tuple = (x, y)
                rock_coords.add(coord_tuple)
    
def print_coords(coords_1, coords_2):
    for y in range(-2, 13) if USE_TEST_DATA else range(-2, 200):
        rocks = ""
        for x in range(480, 522) if USE_TEST_DATA else range(450, 520):
            if (x, y) == (500, 0):
                rocks += '+'
            elif (x, y) in coords_1:
                rocks += '#'
            elif (x, y) in coords_2:
                rocks += 'o'
            else:
                rocks += '.'
        print(rocks)

def get_sand_rest_place(rock_coords, sand_coords, sand_position, maximum_y_value, part):
    sand_x = sand_position[0]
    sand_y = sand_position[1]

    # If outside a lower bounds, return 0
    if part == 1 and sand_y > maximum_y_value:
        return 0
        
    # If position below is free, go to that and iterate
    if not (sand_x, sand_y+1) in sand_coords and not (sand_x, sand_y+1) in rock_coords:
        get_sand_rest_place(rock_coords, sand_coords, (sand_x, sand_y+1), maximum_y_value, part)


    # If below and left are free, go to that and iterate
    if not (sand_x-1, sand_y+1) in sand_coords and not (sand_x-1, sand_y+1) in rock_coords:
        get_sand_rest_place(rock_coords, sand_coords, (sand_x-1, sand_y+1), maximum_y_value, part)

    # If below and right are free, go to that and iterate
    if not (sand_x+1, sand_y+1) in sand_coords and not (sand_x+1, sand_y+1) in rock_coords:
        get_sand_rest_place(rock_coords, sand_coords, (sand_x+1, sand_y+1), maximum_y_value, part)
    
    # else, it rests here
    sand_coords.add(sand_position)
    print(len(sand_coords))
    return

    
def part_1(part):
    rock_corners = []
    maximum_y_value = 0

    for line in input_list:
        line = line.split(' ')
        rock = []
        for word in line:
            if word != '->':
                corner = Corner(word)
                rock.append(corner)
                maximum_y_value = max(maximum_y_value, corner.y)
        rock_corners.append(rock)
    

    rock_coords = set()
    for rock in rock_corners:
        add_rock_to_rock_set(rock, rock_coords)

    if part == 2:
        y_value = maximum_y_value + 2
        x_start = 500 - y_value
        x_end = 500 + y_value
        rock = [Corner('' + str(x_start) + ',' + str(y_value)), Corner('' + str(x_end) + ',' + str(y_value))]
        add_rock_to_rock_set(rock, rock_coords)
    
    print('max', maximum_y_value)

    sand_coords = set()

    get_sand_rest_place(rock_coords, sand_coords, START_TUPLE, maximum_y_value, part)    
    print_coords(rock_coords, sand_coords) 
            
    return len(sand_coords)




print(part_1(2))
# print(part_1(1))
# print(part_1(2))
# print(part_1(2))
