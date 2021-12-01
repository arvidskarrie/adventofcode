
from itertools import combinations 
import re
from collections import Counter
import string
from copy import deepcopy

def rotate_tile(tile, rotation):
    if rotation == 0:
        return tile
    new_tile = deepcopy(tile)
    for i in range(10):
        new_tile[0][i] = tile[9-i][0]
        new_tile[9][i] = tile[9-i][9]
        new_tile[i][0] = tile[9][i]
        new_tile[i][9] = tile[0][i]
    return rotate_tile(new_tile, rotation-1)


def extract(lst, num): 
    return [item[num] for item in lst] 

def part_1():
    tile_list = []
    tile_regex = r'Tile (.*):'
    
    #with open("input.txt") as file:
    with open("input_test.txt") as file:
        line = file.readline()
        while line:

            tile_number = re.findall(tile_regex, line)
            if tile_number == []:
                break

            tile = []
            
            for line in file:
                if line == '\n':
                    tile_list.append([tile_number, tile])
                    line = file.readline()
                    break
                else:
                    tile.append(list(line.rstrip()))

    # Setup brute force test lists
    input_combinations = combinations(range(0, 10), 10)

    for combo in input_combinations:
        test_combination(input_combinations)
    tile = tile_list[0][1]
    rot = rotate_tile(tile, 2)
    return(0)

    #rotate_tile(tile_list[0][1], 1)




print(part_1()) # 25190263477799
#print(part_2()) # 297139939002972