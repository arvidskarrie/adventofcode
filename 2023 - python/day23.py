
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
from itertools import combinations
import aocd

USE_TEST_DATA = 0
TEST_DATA = '1,0,1~1,2,1\n0,0,2~2,0,2\n0,2,3~2,2,3\n0,0,4~0,2,4\n2,0,5~2,2,5\n0,1,6~2,1,6\n1,1,8~1,1,9'

longest_path = 0

def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        with open("input.txt") as _file:
            input_list = [line.strip() for line in _file]
    

    def continue_walk(path_so_far, current_pos):
        global longest_path
        while True:
            x, y = current_pos

            # Return if finished
            if y == len(input_list) - 1:
                # print("One alternative finished: {}".format(len(path_so_far) - 1))
                return len(path_so_far) - 1
                
            # Only keep valid neighbours
            neighbours = [(x + 1, y), (x -1, y), (x, y + 1), (x, y - 1)]
            neighbours = [(x_n, y_n) for x_n, y_n in neighbours if (not (x_n, y_n) in path_so_far and input_list[y_n][x_n] != "#")]

            if not neighbours:
                return 0
            if len(neighbours) == 1:
                current_pos = neighbours[0]
                path_so_far.add(current_pos)
            else:
                # Test all alternatives and return the maximum path
                for temp_current_pos in neighbours:
                    temp_path_so_far = path_so_far.copy()
                    temp_path_so_far.add(temp_current_pos)
                    path = continue_walk(temp_path_so_far, temp_current_pos)
                    if path > longest_path:
                        print("New longest path {}".format(path))
                        longest_path = path
                return longest_path     
            

    # positions are (x, y)
    start_pos = (input_list[0].find("."), 0)
    second_pos = (start_pos[0], 1)
    
    path_so_far = set([start_pos, second_pos])

    print(continue_walk(path_so_far, second_pos))




part_1()