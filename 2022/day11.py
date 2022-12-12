
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations
import aocd
import re

USE_TEST_DATA = 0

class Monkey:
    def __init__(self, item_list, operation, test_result, common):
        self.item_list = item_list
        self.operation = operation
        self.test_result = test_result
        self.inspections = 0
        self.common = common

    def investigate_and_pop_first_item(self, part):
        first_item = self.item_list[0]
        if part == 1:
            worry_level = int(self.operation(first_item) / 3)
        else:
            worry_level = int(self.operation(first_item))

        worry_level %= self.common

        new_monkey = self.test_result(worry_level)
        if len(self.item_list) == 1:
            self.item_list = []
        else:
            self.item_list = self.item_list[1:]
        self.inspections += 1
        return worry_level, new_monkey

    def add_to_list(self, value):
        self.item_list.append(value)

    def is_empty(self):
        return self.item_list == []


if USE_TEST_DATA:
    common_denominator = 23 * 19 * 13 * 17
    input_monkeys = [
        Monkey([79, 98], lambda old: old * 19, lambda x: (2 if x % 23 == 0 else 3), common_denominator),
        Monkey([54, 65, 75, 74], lambda old: old + 6, lambda x: (2 if x % 19 == 0 else 0), common_denominator),
        Monkey([79, 60, 97], lambda old: old * old, lambda x: (1 if x % 13 == 0 else 3), common_denominator),
        Monkey([74], lambda old: old + 3, lambda x: (0 if x % 17 == 0 else 1), common_denominator)
    ]
else:
    common_denominator = 3 * 11 * 7 * 2 * 19 * 5 * 17 * 13
    input_monkeys = [
        Monkey([56, 56, 92, 65, 71, 61, 79], lambda old: old * 7, lambda x: (3 if x % 3 == 0 else 7), common_denominator),
        Monkey([61, 85], lambda old: old + 5, lambda x: (6 if x % 11 == 0 else 4), common_denominator),
        Monkey([54, 96, 82, 78, 69], lambda old: old * old, lambda x: (0 if x % 7 == 0 else 7), common_denominator),
        Monkey([57, 59, 65, 95], lambda old: old + 4, lambda x: (5 if x % 2 == 0 else 1), common_denominator),
        Monkey([62, 67, 80], lambda old: old * 17, lambda x: (2 if x % 19 == 0 else 6), common_denominator),
        Monkey([91], lambda old: old + 7, lambda x: (1 if x % 5 == 0 else 4), common_denominator),
        Monkey([79, 83, 64, 52, 77, 56, 63, 92], lambda old: old + 6, lambda x: (2 if x % 17 == 0 else 0), common_denominator),
        Monkey([50, 97, 76, 96, 80, 56], lambda old: old + 3, lambda x: (3 if x % 13 == 0 else 5), common_denominator)
        ]

def part_1(part):
    # Initiate monkeys
    monkeys = input_monkeys

    # Every round
    if part == 1:
        rounds = 20
    else:
        rounds = 10000
    for _round in range(rounds):
        for monkey in monkeys:
            while True:
                if monkey.is_empty():
                    break
                # Investigate items, increase value, divide by three
                (item_value, target_monkey) = monkey.investigate_and_pop_first_item(part)
                
                # Throw depending on condition
                monkeys[target_monkey].add_to_list(item_value)
    
    for monkey in monkeys:
        print('inspection number = ', monkey.inspections)
    return monkeys[0].inspections == 101

    

#print(part_1(1))
print(part_1(2))
