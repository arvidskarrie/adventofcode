
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
import aocd
import re
import math
import collections
import itertools
import functools
import time

USE_TEST_DATA = 0
TEST_DATA = 'px{a<2006:qkq,m>2090:A,rfg}\npv{a>1716:R,A}\nlnx{m>1548:A,A}\nrfg{s<537:gd,x>2440:R,A}\nqs{s>3448:A,lnx}\nqkq{x<1416:A,crn}\ncrn{x>2662:A,R}\nin{s<1351:px,qqz}\nqqz{s>2770:qs,m<1801:hdj,R}\ngd{a>3333:R,R}\nhdj{m>838:A,pv}\n\n{x=787,m=2655,a=1222,s=2876}\n{x=1679,m=44,a=2067,s=496}\n{x=2036,m=264,a=79,s=2244}\n{x=2461,m=1339,a=466,s=291}\n{x=2127,m=1623,a=2188,s=1013}'

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

def create_functions(tests_data: list[tuple]):
    test_list = []
    for test_data in tests_data:
        (variable, op, num_value, result) = test_data
        variable_idx = idx_dict[variable]
        num_value = int(num_value)  # Convert num_value to int once and for all


        if op == '<':
            fun = lambda x, idx=variable_idx, val=num_value: x[idx] < val
        else:
            assert op == '>', f"Unsupported operator: {op}"
            fun = lambda x, idx=variable_idx, val=num_value: x[idx] > val
        test_list.append((fun, result))

    return test_list

def evaluate_lambda_list(part, fun_list, end_result):
    for (fun, result_if_true) in fun_list:
        if fun(part):
            return result_if_true
    return end_result


def evaluate_data(part, lambda_dict):
    lambda_name = "in"
    while True:
        fun_list, end_result = lambda_dict[lambda_name]

        result = evaluate_lambda_list(part, fun_list, end_result)
        if result in ['A', 'R']:
            return result
        else:
            lambda_name = result


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

    total_accepted_sum = 0
    for line in parts[1]:
        # Evaluate each line
        data = list(re.findall(NUMBERS_REGEX, line))
        data = list(map(int, data))
        result = evaluate_data(data, lambda_dict)
        if result == 'A':
            total_accepted_sum += sum(data)
        else:
            assert result == 'R'

    print(total_accepted_sum)

    # part 2
    # Test a recursive solution
    # Instead 


    pass

    


part_1()
