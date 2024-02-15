
from itertools import combinations 
import re
from collections import Counter
import string

DONE = 'DONE'
GOAL_KEY = 'GOAL_KEY'
GOAL_VALUE = [[1, 'shiny gold']]

def find_in_dict(dictionary, requested_value):
    matches = []
    for key, value_list in dictionary.items():
        for value in value_list:
            if requested_value in value:
                matches.append(key)
                chain_matches = find_in_dict(dictionary, key)
                if chain_matches != []:
                    for item in chain_matches:
                        matches.append(item)
                #matches.append(item for sublist in chain_matches for item in sublist)

    return matches

def get_how_many_bags_it_contains(dictionary, key):
    value = dictionary[key]
    total_number_of_bags = 0
    for bag_type in value:
        multiplicity = int(bag_type[0])
        bag_kind = bag_type[1]


        if bag_kind == DONE:
            total_number_of_bags += multiplicity
        else:
            dictionary[bag_kind]
            contains = get_how_many_bags_it_contains(dictionary, bag_kind)
            total_number_of_bags += multiplicity * contains

    dictionary[key] = [[total_number_of_bags, DONE]]
    return total_number_of_bags + 1


def part_1():
    bag_data = {}

    regex_first_term = '^(.*) bags contain'
    regex_other_term = '([0-9]+ .*?) bag'
    #regex_first_term = re.findall('^(.*) bags contain')

    with open("input.txt") as file:
    #with open("input_test.txt") as file:
        for line in file:
            first_term = re.findall(regex_first_term, line)
            other_term = re.findall(regex_other_term, line)
            bag_data[first_term[0]] = other_term

    matches = find_in_dict(bag_data, 'shiny gold')
    unique_list = list(dict.fromkeys(matches))
    return len(unique_list)
    
def part_2():
    bag_data = {}
    bag_data[GOAL_KEY] = GOAL_VALUE 

    regex_first_term = '^(.*) bags contain'
    regex_other_term = '([0-9]+) (.*?) bag'
    #regex_first_term = re.findall('^(.*) bags contain')

    with open("input.txt") as file:
    #with open("input_test.txt") as file:
        for line in file:
            first_term = re.findall(regex_first_term, line)
            other_term_tuple = list(re.findall(regex_other_term, line))
            other_term_list = []
            for a_tuple in other_term_tuple:
                other_term_list.append(list(a_tuple))
            if other_term_list == []:
                bag_data[first_term[0]] = [[0, DONE]]
            else:
                bag_data[first_term[0]] = other_term_list


    bag_data[GOAL_KEY] = [[get_how_many_bags_it_contains(bag_data, GOAL_KEY), DONE]]
    
    print(bag_data)
    return bag_data[GOAL_VALUE[0][1]][0][0]
    #return get_how_many_bags_it_contains(bag_data, 'shiny gold')

#print(part_1()) # 155
print(part_2()) # 3232