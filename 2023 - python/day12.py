
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
import aocd
import re
import math
import collections
import itertools
import functools

USE_TEST_DATA = 0
TEST_DATA = '???.### 1,1,3\n.??..??...?##. 1,1,3\n?#?#?#?#?#?#?#? 1,3,1,6\n????.#...#... 4,1,1\n????.######..#####. 1,6,5\n?###???????? 3,2,1'


@functools.lru_cache(maxsize=None)  # Cache unlimited items
def get_no_of_arr(current_string: str, damages_list: tuple[int], current_streak: int) -> int:
        # Exit if the number of required damages are higher than existing # and ?
        # Exit if the number of existing # is higher than required damages
        no_of_required_damages = sum(damages_list)
        no_of_existing_damages = current_string.count("#") + current_streak
        no_of_unknowns = current_string.count("?")

        # Check if the arrangement is impossible due to damage constraints
        if not no_of_existing_damages <= no_of_required_damages <= no_of_existing_damages + no_of_unknowns:
            return 0

        # Check if we can successfully close the current streak
        if not damages_list or damages_list == (current_streak, ):
            return 1        

        # Check if the current streak exceeds the required streak
        if damages_list[0] < current_streak:
            return 0

        if current_string.startswith('#'):
            return get_no_of_arr(current_string[1:], damages_list, current_streak + 1)

        if current_string.startswith('.'):
            if current_streak == 0:
                # Streak already closed
                return get_no_of_arr(current_string.lstrip("."), damages_list, 0)
            elif current_streak == damages_list[0]:
                # Close the streak and remove the finished damage
                return get_no_of_arr(current_string.lstrip("."), damages_list[1:], 0)
            else:
                # Current streak is not as high as expected
                return 0

        if current_string.startswith('?'):
            # Recurse with both options and add the result
            return sum([
                 get_no_of_arr(test_char + current_string[1:], damages_list, current_streak)
                 for test_char in ["#", "."]
            ])

        assert False

def prepare_and_run(line):
        split_line = line.split(" ")
        damages_list = list(map(int, split_line[1].split(",")))

        multi_current_string = "?".join([split_line[0] for _ in range(5)]).strip(".")
        multi_damages_list = damages_list[:] * 5

        return get_no_of_arr(multi_current_string, tuple(multi_damages_list), 0)


def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data().splitlines()

    no_of_arr = sum([
        prepare_and_run(line)
        for line in input_list
    ])
        
    assert (15454556629917 == no_of_arr)
    print(15454556629917 == no_of_arr)

part_1()