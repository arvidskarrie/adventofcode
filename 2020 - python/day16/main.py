
from itertools import combinations 
import re
from collections import Counter
import string
from copy import deepcopy
from math import gcd

def part_1():
    accepted_intervals = []
    numbers = []
    error_rate = 0
    
    #with open("input_test.txt") as file:
    with open("input.txt") as file:
        for line in file:
            if line == "\n":
                break
            line = re.split(' ', line.rstrip())
            for word in line:
                if '-' in word:
                    accepted_intervals.append(re.split('-', word))
        
        for line in file:
            if line == "\n" or "ticket" in line:
                continue
            line = re.split(',', line.rstrip())
            for word in line:
                numbers.append(int(word))
        error_rate = sum(numbers)

        for number in numbers:
            for [minm, maxm] in accepted_intervals:
                if int(minm) <= number <= int(maxm):
                    error_rate -= number
                    break
            #print(number)

    return error_rate

def get_approved_tickets(accepted_dict, ticket_list):
    accepted_tickets = []

    for ticket in ticket_list:
        approved_numbers = 0
        for number in ticket:
            number = int(number)

            break_outer = False
            for accepted_intervals in accepted_dict.values():
                for [minm, maxm] in accepted_intervals:
                    if int(minm) <= number <= int(maxm):
                        approved_numbers += 1
                        break_outer = True
                        break
                if break_outer:
                    break
                
        if approved_numbers == len(ticket):
            accepted_tickets.append(ticket)
    return accepted_tickets

def get_field_numbers(accepted_tickets, ticket_field):
    numbers = []
    for ticket in accepted_tickets:
        numbers.append(int(ticket[ticket_field]))
    return numbers

def all_numbers_in_range(field_numbers, field_ranges):
    [[minm1, maxm1], [minm2, maxm2]] = field_ranges
    for number in field_numbers:
        if (minm1 <= number <= maxm1) or (minm2 <= number <= maxm2):
            continue
        else:
            return False
    return True

def part_2(field):
    ticket_list = []
    fields = []
    accepted_dict = {}

    regex_terms = '(.*): (.*)-(.*) or (.*)-(.*)'


    #with open("input_test.txt") as file:
    with open("input.txt") as file:
        for line in file:
            if line == "\n":
                break

            terms = re.findall(regex_terms, line)
            terms = list(terms[0])
            accepted_dict[terms[0]] = [[int(terms[1]), int(terms[2])], [int(terms[3]), int(terms[4])]]
            fields.append(terms[0])

        for line in file:
            if line == "\n" or "ticket" in line:
                continue
            line = re.split(',', line.rstrip())
            ticket_list.append(line)

    # This part was added after to find final answer
    ans = 1
    for i in [3, 5, 16, 11, 4, 17]:
        ans *= int(ticket_list[0][i])
    print(ans)

    accepted_tickets = get_approved_tickets(accepted_dict, ticket_list)
    number_of_fields = len(fields)

    for i in range(number_of_fields):
        field = fields[i]
        # Find what ticket_field corresponds to departure track
        for ticket_field in range(number_of_fields):
            # Check ticket field for every ticket
            field_numbers = get_field_numbers(accepted_tickets, ticket_field)

            if all_numbers_in_range(field_numbers, accepted_dict[field]):
                print((i), ticket_field)
                #print(field, ticket_field, int(accepted_tickets[0][ticket_field]))



def part_2_b():
    dict_fields = {}
    with open("input_test_2.txt") as file:
        for line in file:
            line = re.split(' ', line.rstrip())
            if line[0] in dict_fields.keys():
                old_line = dict_fields[line[0]]
                old_line.append(int(line[1]))
                dict_fields[line[0]] = old_line
            else:
                dict_fields[line[0]] = [int(line[1])]
    for key in dict_fields.keys():
        print(key, dict_fields[key])



#print(part_1()) # 517
dep_list = [
    'departure location',
    'departure station',
    'departure platform',
    'departure track',
    'departure date',
    'departure time',
    'arrival location',
    'arrival station',
    'arrival platform',
    'arrival track',
    'class',
    'duration',
    'price',
    'route',
    'row',
    'seat',
    'train',
    'type',
    'wagon',
    'zone']
    
    
    
    #dep_list = ['departure location']
#for field in dep_list:
#    part_2(field)
part_2('a')
#part_2_b()