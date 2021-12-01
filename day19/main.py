
from itertools import combinations 
import re
from collections import Counter
import string
from copy import deepcopy

def is_value_done(value):
    for alt in value:
        if any(char.isdigit() for char in alt):
            return False
    return True

def make_string_of_list(string_list):
    return_string = ''
    for string in string_list:
        return_string += string
    return return_string

def add_string_and_list(fin_string, val_list):
    string_list = []
    for val_1 in fin_string:
        for val_2 in val_list:
            string_list.append(val_1 + val_2)

    return string_list

def get_finished_value(value_list):
    if not type(value_list) is list:
        return value_list

    num_values = len(value_list)

    if num_values == 1:
        return value_list


    for value in value_list:
        if type(value) is list:
            num_values = len(value)
            if num_values == 1:
                value = value[0]
            else:
                value = make_string_of_list(value)
        
        finished_string_list = value
    
    return finished_string_list

def has_inner_lists(letter_list):
    for letter in letter_list:
        if type(letter) is list:
            return True
    return False

def resolve_inner_letter_list(letter_list):
    resolved = refine_letter_list(letter_list)
    return resolved

def copy_list(resulting_letter_list, num_copies):
    new_list = []
    for _i in range(num_copies):
        for lists in resulting_letter_list:
            new_list.append(deepcopy(lists))

    return new_list

def refine_letter_list2(letter_list):
    if has_inner_lists(letter_list):
        for letter_idx in range(len(letter_list)):
            resolved_list = resolve_inner_letter_list(letter_list[letter_idx])
            letter_list[letter_idx] = resolved_list
    
    resulting_letter_list = ['']



    for letter in letter_list:
        if type(letter) is list:
            # Alternatives
            num_copies = len(letter)
            prev_num_copies = len(resulting_letter_list)
            resulting_letter_list = copy_list(resulting_letter_list, num_copies)

            for i in range(num_copies * prev_num_copies):
                resulting_letter_list[i] += letter[i % num_copies]

        else:
            for i in range(len(resulting_letter_list)):
                resulting_letter_list[i] += letter


    return resulting_letter_list

def part_1():
    match_dict = {}
    alternatives_list = []
    
    #with open("input.txt") as file:
    with open("input_test.txt") as file:
        for line in file:
            if line == '\n':
                break
            
            line = re.split(': ', line.rstrip())
            key = line[0]
            values = line[1]

            if values == '"a"' or values == '"b"':
                values = values[1]
            else:
                values = re.split(' \| ', values)
                for alt_idx in range(len(values)):
                    values[alt_idx] = re.split(' ', values[alt_idx])

            match_dict[key] = values

        # Save alternatives
        for line in file:
            alternatives_list.append(line.rstrip())

    # Iterate through dict and replace
    for key in match_dict.keys():
        value = match_dict[key]
        if is_value_done(value):
            continue
        else:
            for alt_idx in range(len(value)):
                for alt_part_idx in range(len(value[alt_idx])):
                    part_value = value[alt_idx][alt_part_idx]
                    if part_value != 'a' and part_value != 'b':
                        value[alt_idx][alt_part_idx] = match_dict[part_value]
    
    for key in match_dict.keys():
        value = match_dict[key]
        match_dict[key] = get_finished_value(value)
            


    return match_dict, alternatives_list



def outer_letter_list_refinement(letter_list):


#def refine_letter_list(letter_list):




#print(refine_letter_list(['a']), ['a'])
#print(refine_letter_list(['a', 'b']), ['ab'])
#print(outer_letter_list_refinement([['a', 'b'], ['b', 'a']]), ['ab', 'ba'])
print(outer_letter_list_refinement([['a'], ['b']])

print(part_1()) # 25190263477788
#print(part_2()) # 297139939002972