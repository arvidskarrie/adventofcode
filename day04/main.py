
from itertools import combinations 
import re
from collections import Counter
import string

EYE_OK = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def part_1():
    passport_data = []
    number_of_valid_passports = 0

    #Save all data as dict and enter into list
    individual_passport_data = {}
    #with open("input.txt") as _file:
    with open("input_test.txt") as _file:
        for line in _file:
            if line == '\n':
                passport_data.append(individual_passport_data)
                individual_passport_data = {}
            else:
                line.rstrip()
                field = line[0:3]
                value = line[4:-1]
                if field != 'cid':
                    individual_passport_data[field] = value
    

    for passport in passport_data:
        if len(passport) == 7:
            number_of_valid_passports += 1

    print(number_of_valid_passports)

def part_2():
    passport_data = []
    number_of_valid_passports = 0

    #Save all data as dict and enter into list
    individual_passport_data = {}
    with open("input.txt") as _file:
    #with open("input_test.txt") as _file:
        for line in _file:
            if line == '\n':
                passport_data.append(individual_passport_data)
                individual_passport_data = {}
            else:
                line.rstrip()
                field = line[0:3]
                value = line[4:-1]
                if field != 'cid':
                    individual_passport_data[field] = value
    

    for passport in passport_data:
        if len(passport) != 7:
            continue
        hgt = passport['hgt']
        if 'cm' in hgt:
            hgt_ok = (150 <= int(hgt[:-2]) <= 193)
        elif 'in' in hgt:
            hgt_ok = (59 <= int(hgt[:-2]) <= 76)
        else:
            hgt_ok = False
        hcl = passport['hcl']
        hcl_ok = (len(hcl) == 7 and hcl[0] == '#' and all(c in string.hexdigits for c in hcl[1:]))

        pid = passport['pid']
        pid_ok = (len(pid) == 9 and all(c in string.digits for c in pid))

        if ((1920 <= int(passport['byr']) <= 2002) and
            (2010 <= int(passport['iyr']) <= 2020) and
            (2020 <= int(passport['eyr']) <= 2030) and
            (hgt_ok) and
            (hcl_ok) and
            (passport['ecl'] in EYE_OK) and
            (pid_ok)):
            number_of_valid_passports += 1

    print(number_of_valid_passports)


#part_1()
part_2()