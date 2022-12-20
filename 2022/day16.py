
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations, permutations
from functools import lru_cache
import aocd
import re


USE_TEST_DATA = 0
TEST_DATA = 'Valve AA has flow rate=0; tunnels lead to valves DD, II, BB\nValve BB has flow rate=13; tunnels lead to valves CC, AA\nValve CC has flow rate=2; tunnels lead to valves DD, BB\nValve DD has flow rate=20; tunnels lead to valves CC, AA, EE\nValve EE has flow rate=3; tunnels lead to valves FF, DD\nValve FF has flow rate=0; tunnels lead to valves EE, GG\nValve GG has flow rate=0; tunnels lead to valves FF, HH\nValve HH has flow rate=22; tunnel leads to valve GG\nValve II has flow rate=0; tunnels lead to valves AA, JJ\nValve JJ has flow rate=21; tunnel leads to valve II'
START_VALVE_NAME = 'AA'
if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
else:
    input_list = aocd.get_data(day=16).splitlines()


input_regex = r'Valve (.*) has flow rate=(.*); tunnel(?:s)? lead(?:s)? to valve(?:s)? (.*)'

class Valve:
    def __init__(self, value_list):
        self.name = value_list[0]
        self.flow = int(value_list[1])
        self.conn_map = {}
        for conn in value_list[2].split(', '):
            self.conn_map[conn] = 1
        self.open = False

def part_1(part):
    valves = {}
    for line in input_list:
        terms = re.findall(input_regex, line)
        terms = list(terms[0])
        
        valve = Valve(terms)
        valves[valve.name] = valve
    
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

    flow = {}
    neighbours = {}
    for valve in valves.values():
        flow[valve.name] = valve.flow
        neighbours[valve.name] = valve.conn_map

    # curr_pos = string with name
    # open_sorted_tuple = tuple with all already opened strings
    # time_left = int with time left
    
    # flow = dict with all flow values
    # neighbours = dict matching neighbours names
    @lru_cache(maxsize=None)
    def calc_maxflow(curr_pos, open_sorted_tuple, time_left, elephant_active):
        best = 0
        if time_left <= 0:
            if elephant_active:
                return best
            else:
                return calc_maxflow(START_VALVE_NAME, open_sorted_tuple, 26, True)
        
        # If closed, we could open the valve
        if not curr_pos in open_sorted_tuple:
            # Calculate with new tuple and one minute less
            unsorted_tuple = open_sorted_tuple + (curr_pos,)
            new_open_set = tuple(sorted(unsorted_tuple))
            gain = flow[curr_pos] * (time_left - 1) # new gain from valve
            best = calc_maxflow(curr_pos, new_open_set, time_left - 1, elephant_active) + gain
        
        # Iterate over neighbours and choose the best result
        for n_pos, n_time in neighbours[curr_pos].items():
            best = max(best, calc_maxflow(n_pos, open_sorted_tuple, time_left - n_time, elephant_active))

        # Or do nothing
        # If elephant is not active, it will become active
        # Otherwise, we will return nothing
        best = max(best, calc_maxflow(n_pos, open_sorted_tuple, 0, elephant_active))

        return best

    return calc_maxflow(START_VALVE_NAME, (START_VALVE_NAME,), 26 if part == 2 else 30, part == 1)

# print(part_1(1)) # 1651 if test, else 1595
print(part_1(2)) # Should be 1707
