
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
import aocd
import re
import math
import collections
import itertools
import functools
import time
import copy

USE_TEST_DATA = 0
TEST_DATA = 'px{a<2006:qkq,m>2090:A,rfg}\npv{a>1716:R,A}\nlnx{m>1548:A,A}\nrfg{s<537:gd,x>2440:R,A}\nqs{s>3448:A,lnx}\nqkq{x<1416:A,crn}\ncrn{x>2662:A,R}\nin{s<1351:px,qqz}\nqqz{s>2770:qs,m<1801:hdj,R}\ngd{a>3333:R,R}\nhdj{m>838:A,pv}\n\n{x=787,m=2655,a=1222,s=2876}\n{x=1679,m=44,a=2067,s=496}\n{x=2036,m=264,a=79,s=2244}\n{x=2461,m=1339,a=466,s=291}\n{x=2127,m=1623,a=2188,s=1013}'
# TEST_DATA = 'px{a<2006:qkq,m>2090:A,rfg}\npv{a>1716:R,A}\nlnx{m>1548:A,A}\nrfg{s<537:gd,x>2440:R,A}\nqs{s>3448:A,lnx}\nqkq{x<1416:A,crn}\ncrn{x>2662:A,R}\nin{s<1351:px,qqz}\nqqz{s>2770:qs,m<1801:hdj,R}\ngd{a>3333:R,R}\nhdj{m>838:A,pv}\n\n{x=787,m=2655,a=1222,s=2876}\n{x=1679,m=44,a=2067,s=496}\n{x=2036,m=264,a=79,s=2244}\n{x=2461,m=1339,a=466,s=291}\n{x=2127,m=1623,a=2188,s=1013}'

NAME_REGEX = r"^(?P<flow_name>.*)\{"
TESTS_REGEX = r"(?P<variable>[A-Za-z])(?P<op>[<>])(?P<num_val>\d+):(?P<result>[A-Za-z]+)"
END_REGEX = r",(?P<else>[A-Za-z]+)\}$"
NUMBERS_REGEX = r"(\d+)"


idx_dict = {
    'x': 0,
    'm': 1,
    'a': 2,
    's': 3,
}

def sort_into_parts(data: list[str]) -> list[list[str]]:
    return [part.split("\n") for part in "\n".join(data).split("\n\n")]


class Combination:
    def __init__(self, start_lambda_name):
       self.start = start_lambda_name
       self.min_values = [1, 1, 1, 1] # inclusive
       self.max_values = [4001, 4001, 4001, 4001] # exclusive

    def __copy__(self):
        new_obj = Combination(self.start)
        new_obj.min_values = self.min_values[:]
        new_obj.max_values = self.max_values[:]
        return new_obj


def create_functions(tests_data: list[tuple]):
    test_list = []
    for test_data in tests_data:
        (variable, op, num_value, result) = test_data
        variable_idx = idx_dict[variable]
        num_value = int(num_value)  # Convert num_value to int once and for all

        if op == '<':
            fun = lambda x, idx=variable_idx, val=num_value: x.min_values[idx] < val
            split_value = num_value
        else:
            assert op == '>', f"Unsupported operator: {op}"
            fun = lambda x, idx=variable_idx, val=num_value: x.min_values[idx] > val
            split_value = num_value + 1

        # split_value is the lowest value that is in the top interval
        test_list.append((variable_idx, split_value, fun, result))
    
    return test_list

# Either return a result, or if needed, split the combnation and return the parts
def evaluate_lambda_list(combo: Combination, fun_list, end_result):
    for (variable_idx, split_value, fun, result_if_true) in fun_list:
        # Split needed if split value is in the interval, but not the lowest value
        if combo.min_values[variable_idx] < split_value < combo.max_values[variable_idx]:
            first_combo = copy.copy(combo)
            first_combo.max_values[variable_idx] = split_value
            second_combo = copy.copy(combo)
            second_combo.min_values[variable_idx] = split_value
            return None, [first_combo, second_combo]

        # If no split, evaluate with either min or max, since they will give the same result
        if fun(combo):
            return result_if_true, []
    return end_result, []


def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        with open("input.txt") as _file:
            input_list = [line.strip() for line in _file]

    parts = sort_into_parts(input_list)

    lambda_dict = {}
    # Create lambda functions
    for line in parts[0]:
        name = re.search(NAME_REGEX, line).group('flow_name')
        tests = re.findall(TESTS_REGEX, line)
        else_flow = re.search(END_REGEX, line).group('else')

        lambda_dict[name] = (create_functions(tests), else_flow)

    # part 2
    # Test a recursive solution
    # Evaluate a range of values. Whenever any split occurs, split the combination and move on

    start_comb = Combination('in')
    combinations_to_try = {start_comb}
    accepted_no_of_combinations = 0
    while len(combinations_to_try) > 0:
        print(len(combinations_to_try), accepted_no_of_combinations)
        combo = combinations_to_try.pop()
        lambda_name = combo.start
        while True:
            fun_list, end_result = lambda_dict[lambda_name]

            result, new_combos = evaluate_lambda_list(combo, fun_list, end_result)

            if result == 'A':
                ranges = [combo.max_values[i] - combo.min_values[i] for i in range(4)]
                product = ranges[0] * ranges[1] * ranges[2] * ranges[3]
                accepted_no_of_combinations += product
                break
            if result == 'R':
                break
            elif new_combos != []:
                for new_comb in new_combos:
                    new_comb.start = lambda_name
                    combinations_to_try.add(new_comb)
                break
            
            lambda_name = result


    pass

    


part_1()
