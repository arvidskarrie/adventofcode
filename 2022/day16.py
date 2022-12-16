
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations, permutations
import aocd
import re


USE_TEST_DATA = 1
TEST_DATA = 'Valve AA has flow rate=0; tunnels lead to valves DD, II, BB\nValve BB has flow rate=13; tunnels lead to valves CC, AA\nValve CC has flow rate=2; tunnels lead to valves DD, BB\nValve DD has flow rate=20; tunnels lead to valves CC, AA, EE\nValve EE has flow rate=3; tunnels lead to valves FF, DD\nValve FF has flow rate=0; tunnels lead to valves EE, GG\nValve GG has flow rate=0; tunnels lead to valves FF, HH\nValve HH has flow rate=22; tunnel leads to valve GG\nValve II has flow rate=0; tunnels lead to valves AA, JJ\nValve JJ has flow rate=21; tunnel leads to valve II'
START_VALVE_NAME = 'AA'
if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
else:
    input_list = aocd.get_data().splitlines()


input_regex = r'Valve (.*) has flow rate=(.*); tunnel(?:s)? lead(?:s)? to valve(?:s)? (.*)'

class Valve:
    def __init__(self, value_list):
        self.name = value_list[0]
        self.flow = int(value_list[1])
        self.conn_map = {}
        for conn in value_list[2].split(', '):
            self.conn_map[conn] = 1
        self.open = False

def evaluate(combo, valves):
    pressure_released = 0
    last_valve = valves[START_VALVE_NAME]
    countdown = 30
    for part in combo:
        # Travel from last part
        countdown -= last_valve.conn_map[part]

        # Take one minute opening
        countdown -= 1
        valve = valves[part]
        valve.open = True

        # See if time has run out
        if countdown <= 0:
            return pressure_released

        # Add total pressure released
        pressure_released += valve.flow * countdown
        last_valve = valve

    # If path is done, return 
    return pressure_released

def part_1(part):
    valves = {}
    for line in input_list:
        terms = re.findall(input_regex, line)
        terms = list(terms[0])
        
        valve = Valve(terms)
        valves[valve.name] = valve
    
    print(len(valves))


    # Remove valves with no flow
    valves_to_be_deleted = []
    for name, valve in valves.items():
        if valve.flow != 0 or name == START_VALVE_NAME:
            continue
        conn_combs = combinations(valve.conn_map.items(), 2)
        for comb in conn_combs:
            if  (comb[0][0] in valves_to_be_deleted or comb[1][0] in valves_to_be_deleted):
                #remove todo
                continue
            first_valve = valves[comb[0][0]]
            second_valve = valves[comb[1][0]]

            if name in first_valve.conn_map:
                del first_valve.conn_map[name]
            if name in second_valve.conn_map:
                del second_valve.conn_map[name]
            dist = comb[0][1] + comb[1][1]
            # Add new tunnel on the first and second valve
            if (not second_valve.name in first_valve.conn_map) or (first_valve.conn_map[second_valve.name] > dist):
                first_valve.conn_map[second_valve.name] = dist
                second_valve.conn_map[first_valve.name] = dist

        # If a valve has no pressure and all connections have been transferred, it has no use
        valves_to_be_deleted.append(valve)

    # Remove now useless valves:
    for valve in valves_to_be_deleted:
        del valves[valve.name]

    # Create paths betseen all still existing valves
    for name, valve in valves.items():
        conn_combs = combinations(valve.conn_map.items(), 2)
        for comb in conn_combs:
            first_valve = valves[comb[0][0]]
            second_valve = valves[comb[1][0]]
            dist = comb[0][1] + comb[1][1]
            # Add new tunnel on the first and second valve
            if (not second_valve.name in first_valve.conn_map) or (first_valve.conn_map[second_valve.name] > dist):
                first_valve.conn_map[second_valve.name] = dist
                second_valve.conn_map[first_valve.name] = dist
    for valve in valves.values():
        assert len(valve.conn_map) == len(valves) - 1


    # generate all alternatives
    pop_AA = valves.pop(START_VALVE_NAME)
    all_combinations = list(permutations(valves.keys(), len(valves)))
    # all_combinations = list(permutations(valves.keys(), 8))
    valves[pop_AA.name] = pop_AA

    # return len(all_combinations)

    # Iterate through all alternatives
    max_value = 0
    for combo in all_combinations:
        val = evaluate(combo, valves)
        max_value = max(max_value, val)

    return max_value



print(part_1(1)) # 1651
