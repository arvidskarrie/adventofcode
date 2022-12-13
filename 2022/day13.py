
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations
import aocd
import re


USE_TEST_DATA = 0
TEST_DATA = '[1,1,3,1,1]\n[1,1,5,1,1]\n\n[[1],[2,3,4]]\n[[1],4]\n\n[9]\n[[8,7,6]]\n\n[[4,4],4,4]\n[[4,4],4,4,4]\n\n[7,7,7,7]\n[7,7,7]\n\n[]\n[3]\n\n[[[]]]\n[[]]\n\n[1,[2,[3,[4,[5,6,7]]]],8,9]\n[1,[2,[3,[4,[5,6,0]]]],8,9]'

if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
else:
    input_list = aocd.get_data(day=13).splitlines()

def is_pair_in_order(left, right):
    if left == []:
        return True
    elif right == []:
        return False
    if left[0] == right[0]:
        return is_pair_in_order(left[1:], right[1:])
    
    if type(left[0]) == int and type(right[0]) == int:
        return left[0] < right[0]

    if type(left[0]) == list and type(right[0]) == list:
        return is_pair_in_order(left[0], right[0])

    if type(left[0]) == int:
        tmp_left = left.copy()
        tmp_left[0] = [tmp_left[0]]
        return is_pair_in_order(tmp_left, right)
    
    if type(right[0]) == int:
        tmp_right = right.copy()
        tmp_right[0] = [tmp_right[0]]
        return is_pair_in_order(left, tmp_right)
    

def part_1(part):
    list_of_pairs = []
    a_pair = []
    for line in input_list:
        if line == "":
            list_of_pairs.append(a_pair)
            a_pair = []
            continue
        a_pair.append(eval(line))
    list_of_pairs.append(a_pair)

    idx_sum = 0
    for idx, pair in enumerate(list_of_pairs):
        if is_pair_in_order(pair[0], pair[1]):
            idx_sum += (idx+1)

    return idx_sum

def compare(first, second):
    return is_pair_in_order(first, second) - 0.5

class Pair(list):
    def __lt__(self, other):
        if self == [[2]] or other == [[2]]:
            pass
        res = is_pair_in_order(self, other)
        # print(self, other, res)
        return res


def part_2(part):
    input_modified = []
    for line in input_list:
        if line != "":
            input_modified.append(Pair(eval(line)))
    
    input_modified.append(Pair([[2]]))
    input_modified.append(Pair([[6]]))
    
    sorted_list = sorted(input_modified)
    
    for obj in sorted_list:
        print(obj)
    
    place_of_two = sorted_list.index([[2]]) + 1
    place_of_six = sorted_list.index([[6]]) + 1

    return place_of_two * place_of_six
    # return sorted_list



print(part_1(1) == 13)
print(part_2(1))
