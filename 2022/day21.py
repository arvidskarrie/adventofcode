
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations, permutations
from functools import lru_cache
import aocd
import re

input_regex1 = r'(.*): (.*)'

USE_TEST_DATA = 0
TEST_DATA = 'root: pppw + sjmn\ndbpl: 5\ncczh: sllz + lgvd\nzczc: 2\nptdq: humn - dvpt\ndvpt: 3\nlfqf: 4\nhumn: 5\nljgn: 2\nsjmn: drzm * dbpl\nsllz: 4\npppw: cczh / lfqf\nlgvd: ljgn * ptdq\ndrzm: hmdt - zczc\nhmdt: 32'
if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
else:
    input_list = aocd.get_data(day=21).splitlines()
ROOT = 'root'
HUMN = 'humn'
UNKNOWN = 'Unknown'

input_regex_full = r'(.*): (.*) (.*) (.*)'
input_regex_int = r'(.*): (.*)'

class Monkey:
    def __init__(self, data_tuple):
        self.own_name, self.name1, self.op_sign, self.name2 = tuple(data_tuple)



        if self.op_sign == '+':
            self.operation = lambda monkey_dict: monkey_dict[self.name1] + monkey_dict[self.name2]
        elif self.op_sign == '-':
            self.operation = lambda monkey_dict: monkey_dict[self.name1] - monkey_dict[self.name2]
        elif self.op_sign == '*':
            self.operation = lambda monkey_dict: monkey_dict[self.name1] * monkey_dict[self.name2]
        elif self.op_sign == '/':
            self.operation = lambda monkey_dict: monkey_dict[self.name1] // monkey_dict[self.name2]
        
    def set_part_2_op(self):
        self.operation = lambda monkey_dict: monkey_dict[self.name1] == monkey_dict[self.name2]


def part_1(part):
    finished_monkeys_dict = {}
    unfinished_monkeys_list = []
    # all_monkeys = 
    
    for line in input_list:
        terms = re.findall(input_regex_full, line)
        if terms == []:
            # Finished monkey
            terms = re.findall(input_regex_int, line)
            terms = list(terms[0])
            finished_monkeys_dict[terms[0]] = int(terms[1])
        else:
            monkey = Monkey(terms[0])
            if monkey.own_name == ROOT and part == 2:
                monkey.set_part_2_op()
            unfinished_monkeys_list.append(monkey)

    if part == 1:
        while unfinished_monkeys_list:
            for monkey in reversed(unfinished_monkeys_list):
                if monkey.name1 in finished_monkeys_dict and monkey.name2 in finished_monkeys_dict:
                    finished_monkeys_dict[monkey.own_name] = monkey.operation(finished_monkeys_dict)
                    unfinished_monkeys_list.remove(monkey)
        return finished_monkeys_dict[ROOT]
    
    

    
    

    

    

print(part_1(1)) # 353837700405464 / 152
# print(part_1(2)) # 8302
