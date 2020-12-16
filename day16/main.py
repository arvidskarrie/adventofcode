
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

def part_2(field):
    ticket_list = []
    fields = []
    accepted_tickets = []
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

    number_of_fields = len(fields)
    #for field in fields:
    #    if 'departure' in field:

    print(accepted_tickets)
    # Find what ticket_field corresponds to departure track
    for ticket_field in range(number_of_fields):
        # Check ticket field for every ticket
        correct = True
        for ticket in accepted_tickets:
            [[minm1, maxm1], [minm2, maxm2]] = accepted_dict[field]
            ticket_number = int(ticket[ticket_field])
            if not ((minm1 <= ticket_number <= maxm1) or (minm2 <= ticket_number <= maxm2)):
                correct = False
                break
        if correct:
            return int(accepted_tickets[0][ticket_field])

    

print(part_1()) # 517
answer = 1
dep_list = ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time']
dep_list = ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time']
for field in dep_list:
    answer *= part_2(field)
print(answer)