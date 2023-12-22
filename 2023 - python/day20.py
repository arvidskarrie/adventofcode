
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
TEST_DATA = 'broadcaster -> a\n%a -> inv, con\n&inv -> b\n%b -> con\n&con -> output'

FLIP_FLOP_REGEX = r"^%(.*) -> (.*)$"
CONJUNCTION_REGEX = r"^&(.*) -> (.*)$"
BROADCASTER = r"^broadcaster -> (.*)$"

LOW = 0
HIGH = 1

OFF = False
ON = True

class Module:
    def __init__(self, name, receivers):
       self.receivers = receivers
       self.name = name

    def get_receivers(self):
        return self.receivers

class FlipFlop(Module):
    def __init__(self, name, receivers):
       super().__init__(name, receivers)
       self.state = OFF
    
    def trigger(self, _sender, signal):
        if signal == HIGH:
            return []
        
        self.state = not self.state # flip
        new_signal = HIGH if self.state == ON else LOW

        return [
            (self.name, rec, new_signal)
            for rec in self.receivers
        ]


class Conjunction(Module):
    def __init__(self, name, receivers):
        super().__init__(name, receivers)
        self.inputs = {}
    
    def add_input(self, input_name):
        self.inputs[input_name] = LOW
    
    def trigger(self, sender, signal):
        assert sender in self.inputs.keys()
        self.inputs[sender] = signal

        if all(
            input == HIGH
            for input in self.inputs.values()
        ):
            new_signal = LOW
        else: 
            new_signal = HIGH

        return [
            (self.name, rec, new_signal)
            for rec in self.receivers
        ]

    def evaluate(self):
        pass # TODO

class Broadcaster(Module):
    def __init__(self, name, receivers):
       super().__init__(name, receivers)
    
    def trigger(self, sender, signal):
        assert signal == None
        assert sender == None
        return [
            (self.name, rec, LOW)
            for rec in self.receivers
        ]

class Button(Module):
    def __init__(self, name, receivers):
       super().__init__(name, receivers)
    
    def trigger(self, sender, signal):
        assert signal == None
        assert sender == None
        return [
            (self.name, rec, LOW)
            for rec in self.receivers
        ]


def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        with open("input.txt") as _file:
            input_list = [line.strip() for line in _file]

    modules = {}
    modules["button"] = Button("button", ["broadcaster"])

    # Create all modules
    for line in input_list:
        if line == "":
            continue
        first_char = line[0]
        if first_char == "%":
            (name, receivers) = re.findall(FLIP_FLOP_REGEX, line)[0]
            receivers = receivers.split(", ")
            modules[name] = FlipFlop(name, receivers)
        elif first_char == "&":
            (name, receivers) = re.findall(CONJUNCTION_REGEX, line)[0]
            receivers = receivers.split(", ")
            modules[name] = Conjunction(name, receivers)
        elif first_char == "b":
            receivers = re.findall(BROADCASTER, line)[0]
            receivers = receivers.split(", ")
            modules["broadcaster"] = Broadcaster("broadcaster", receivers)
        else:
            assert False 

    
    
    # Go through all modules and add inputs to all conjunctions
    conjunction_names = set([
        key
        for key, val in modules.items() if isinstance(val, Conjunction)
    ])

    for name, module in modules.items():
        receivers = module.get_receivers()
        for rec in receivers:
            if rec in conjunction_names:
                modules[rec].add_input(name)

    for iter in range(10000):
        # Use a stack to keep track of all signals and their order
        # (Sender, To, Signal type)
        stack = [(None, "broadcaster", None)]
        for sender, to_be_triggered, signal in stack:
            # print(sender, signal, to_be_triggered)
            if to_be_triggered == "jq" and signal == HIGH:
                print("{} {}".format(iter+1, sender))
                # Use these values to calculate LCD of when all four is triggered
            if to_be_triggered == "rx" and signal == LOW:
                print(iter + 1)
                exit
            if to_be_triggered in modules.keys():
                new_signals = modules[to_be_triggered].trigger(sender, signal)
                stack += new_signals
part_1()
