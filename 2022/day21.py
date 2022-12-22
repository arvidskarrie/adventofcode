
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

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

def part_1():
    # finished_monkeys_dict = {}
    # unfinished_monkeys_list = []
    all_monkeys = {}

    class Monkey:
        def __init__(self, name, value, other_monkey_1 = UNKNOWN, other_monkey_2 = UNKNOWN, op_sign = UNKNOWN):
            self.name = name
            self.value = value
            self.other_monkey_1 = other_monkey_1
            self.other_monkey_2 = other_monkey_2
            self.op_sign = op_sign
        
        def update_monkeys(self):
            if self.other_monkey_1 != UNKNOWN:
                self.other_monkey_1 = all_monkeys[self.other_monkey_1]
            if self.other_monkey_2 != UNKNOWN:
                self.other_monkey_2 = all_monkeys[self.other_monkey_2]

        def can_it_finish(self):
            if self.name == HUMN:
                return False
            other1 = self.other_monkey_1
            other2 = self.other_monkey_2

            if self.name == ROOT:
                if other1.value != UNKNOWN and other2.value == UNKNOWN:
                    other2.value = other1.value
                if other2.value != UNKNOWN and other1.value == UNKNOWN:
                    other1.value = other2.value
                return other2.value != UNKNOWN and other1.value != UNKNOWN

            if [self.value, other1.value, other2.value].count(UNKNOWN) == 0:
                return True
            elif [self.value, other1.value, other2.value].count(UNKNOWN) > 1:
                return False

            # Exactly one unknown means that the last value can be calculated
            sign = self.op_sign
            if self.value == UNKNOWN:
                if sign == '+':   self.value = other1.value + other2.value
                elif sign == '-': self.value = other1.value - other2.value
                elif sign == '*': self.value = other1.value * other2.value
                elif sign == '/': self.value = other1.value // other2.value
            elif other1.value == UNKNOWN:
                if sign == '+':   other1.value = self.value - other2.value
                elif sign == '-': other1.value = self.value + other2.value
                elif sign == '*': other1.value = self.value // other2.value
                elif sign == '/': other1.value = self.value * other2.value
            elif other2.value == UNKNOWN:
                if sign == '+':   other2.value = self.value - other1.value
                elif sign == '-': other2.value = other1.value - self.value
                elif sign == '*': other2.value = self.value // other1.value
                elif sign == '/': other2.value = other1.value // self.value
            else:
                assert(False)
            return True
    
    for line in input_list:
        terms = re.findall(input_regex_full, line)
        if terms == []:
            # Finished monkey
            terms = re.findall(input_regex_int, line)
            own_name, value = terms[0]
            monkey = Monkey(own_name, int(value))
            if own_name == HUMN:
                monkey.value = UNKNOWN
            all_monkeys[monkey.name] = monkey
        else:
            own_name, name1, op_sign, name2 = terms[0]
            if own_name == ROOT:
                op_sign = '='
            own_name, name1, op_sign, name2 = terms[0]
            monkey = Monkey(own_name, UNKNOWN, name1, name2, op_sign)
            all_monkeys[monkey.name] = monkey
    
    not_finished_monkeys_list = []
    for monkey in all_monkeys.values():
        monkey.update_monkeys()
        if monkey.value == UNKNOWN:
            not_finished_monkeys_list.append(monkey)
    
    while True:
        # Break condition
        if all_monkeys[HUMN].value != UNKNOWN:
            return all_monkeys[HUMN].value

        # Loop over all not finished monkeys
        for monkey in reversed(not_finished_monkeys_list):
            # If 2/3 relevant monkeys have value, update the third and consider it done
            print(monkey.name)
            if monkey.can_it_finish():
                print('finished')
                # Add it to finished
                not_finished_monkeys_list.remove(monkey)
                pass

print(part_1()) # 353837700405464 / 152
# print(part_1(2)) # 8302
