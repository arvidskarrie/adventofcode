
from itertools import combinations 
import re
from collections import Counter
import string

def part_2():
    number_of_answers = 0

    #with open("input.txt") as file:
    with open("input_test.txt") as file:
        group_answers = file.readline().rstrip()
        for line in file:
            if line == '\n':
                number_of_answers += len(group_answers)
                group_answers = file.readline().rstrip()
            else:
                group_answers = ''.join(set(group_answers).intersection(line.rstrip()))

    # process last line
    number_of_answers += len(group_answers)

    return number_of_answers

#print(part_1()) # 6443
print(part_2()) # 3232
