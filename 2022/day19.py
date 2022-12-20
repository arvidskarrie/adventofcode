
import os
os.environ["AOC_SESSION"] = "53616c7465645f5feb5f98622da494e1f359f67b2973c8f6a54ed362910e50e251d3f40a7189ffd45624f53a2c2e408b0039c07d21c2423c1ebce73b8d6b4bce"

from itertools import combinations, permutations
from functools import lru_cache
import aocd
import re

USE_TEST_DATA = 0
TEST_DATA = 'Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.\nBlueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.'
if USE_TEST_DATA:
    input_list = TEST_DATA.splitlines()
else:
    input_list = aocd.get_data(day=19).splitlines()

input_regex = r'Blueprint (.*): Each ore robot costs (.*) ore. Each clay robot costs (.*) ore. Each obsidian robot costs (.*) ore and (.*) clay. Each geode robot costs (.*) ore and (.*) obsidian.'

class Blueprint:
    def __init__(self, terms):
        self.id = terms[0]
        ore_robot_cost = (terms[1], 0, 0)
        clay_robot_cost = (terms[2], 0, 0)
        obsidian_robot_cost = (terms[3], terms[4], 0)
        geode_robot_cost = (terms[5], 0, terms[6])
        self.robot_costs = (ore_robot_cost, clay_robot_cost, obsidian_robot_cost, geode_robot_cost)

def can_robot_be_built(inv, cost):
    for idx in range(3):
        if cost[idx] > inv[idx]:
            return False
    return True
def can_all_robots_be_built(inv, cost_list):
    for i in range(4):
        if not can_robot_be_built(inv, cost_list[i]):
            return False
    return True

def pay_price(inv, cost):
    new_inv_tuple = tuple()
    for idx in range(3):
        new_inv_tuple = new_inv_tuple + (inv[idx] - cost[idx],)
    return new_inv_tuple

def mine(rob, inv):
    new_inv_tuple = tuple()
    for idx in range(3):
        new_inv_tuple = new_inv_tuple + (inv[idx] + rob[idx],)
    return new_inv_tuple

def can_we_get_enough_obsidian(obs_robots, obs_needed, obs_currently, time_left):
    # The current robots will produce obs_robots * (time_left - 2) obsidian until round 2
    time_until_2 = time_left - 2
    
    # Our guaranteed amount is current + future
    future_obs_amount = obs_currently + obs_robots * time_until_2

    # No point in creating any new obs_robots
    if time_until_2 <= 1:
        return obs_needed <= future_obs_amount

    # Optimally, we can build robots and harvest (time_until_2 * (time_until_2 - 1) / 2) obsidian
    return obs_needed <= future_obs_amount + (time_until_2 * (time_until_2 - 1) / 2)
    

def part_1(part):
    blueprints = []
    for line in input_list:
        terms = re.findall(input_regex, line)
        terms = list(terms[0])
        terms = list(map(int, terms))
        bp = Blueprint(terms)
        blueprints.append(bp)

    @lru_cache(maxsize=None)
    def calc_max_geode(robots, inventory, time_left):
        best = 0
        if time_left <= 1:
            return best
        if (time_left < 4 and robots[2] == 0):  # tested to remove
            return best
        if (time_left < 5 and robots[1] == 0): # tested to remove
            return best
        if (time_left < 5 and robots[0] == 0): # tested to remove
            return best

        # We need at least robot_costs[3][2] when time_left = 2
        obsidian_needed = robot_costs[3][2]
        no_of_obsidian_robots = robots[2]
        current_obsidian_amount = inventory[2]
        if not can_we_get_enough_obsidian(robots[2], robot_costs[3][2], inventory[2], time_left):
            return best
        
        
        # For every robot we can build, build it and evaluate
        for robot_type in range(4):
            if (time_left < 4 and robot_type == 2):
                continue
            if (time_left < 5 and robot_type == 0):
                continue
            if (time_left < 7 and robot_type == 1):
                continue

            # If the number of robots are already at max needed, do not build more
            if robot_type != 3 and robots[robot_type] >= max_robots_needed[robot_type]:
                continue

            if can_robot_be_built(inventory, robot_costs[robot_type]):
                # Pay the price
                new_inv = pay_price(inventory, robot_costs[robot_type])

                # Mine
                new_inv = mine(robots, new_inv)

                if robot_type == 3:
                    # Calculate potential gain
                    gain = time_left - 1
                    new_robots = robots
                else:
                    # Add the robot
                    gain = 0
                    new_robots = list(robots)
                    new_robots[robot_type] += 1
                    new_robots = tuple(new_robots)

                # Evaluate future
                best = max(best, calc_max_geode(new_robots, new_inv, time_left - 1) + gain)

        # If we can build all types of robots, we must build one:
        if not can_all_robots_be_built(inventory, robot_costs):
            # Evaluate if we do not build
            new_inv = mine(robots, inventory)
            best = max(best, calc_max_geode(robots, new_inv, time_left - 1))

        # Return best
        return best

    total_value = 0
    total_cycles = 0
    for bp in blueprints:
        calc_max_geode.cache_clear()
        inventory = (0, 0, 0)
        robots = (1, 0, 0)
        time_left = 24
        robot_costs = bp.robot_costs
        max_robots_needed = {0: 0, 1: 0, 2: 0}
        for robot in robot_costs:
            for idx, cost in enumerate(robot):
                max_robots_needed[idx] = max(max_robots_needed[idx], cost)

        best_value = calc_max_geode(robots, inventory, time_left)


        print(bp.id, best_value * bp.id)
        total_value += best_value * bp.id
        total_cycles += calc_max_geode.cache_info().currsize
        print(calc_max_geode.cache_info())
    print('total cycles', total_cycles)
    return total_value

print(part_1(1))
