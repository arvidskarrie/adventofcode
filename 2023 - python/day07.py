
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
import aocd
import re
import math
import collections

USE_TEST_DATA = 0
TEST_DATA = '32T3K 765\nT55J5 684\nKK677 28\nKTJJT 220\nQQQJA 483'

FIVE_OF_A_KIND = (5,)
FOUR_OF_A_KIND = (4, 1)
FULL_HOUSE = (3, 2)
THREE_OF_A_KIND = (3, 1, 1)
TWO_PAIRS = (2, 2, 1)
PAIR = (2, 1, 1, 1)
NOTHING = (1, 1, 1, 1, 1)

hand_score_dict = {
    FIVE_OF_A_KIND: 7,
    FOUR_OF_A_KIND: 6,
    FULL_HOUSE: 5,
    THREE_OF_A_KIND: 4,
    TWO_PAIRS: 3,
    PAIR: 2,
    NOTHING: 1,
}

card_score_dict = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}

def get_hand_score(hand: str):
    card_count = list(collections.Counter(list(hand)).values())
    card_count.sort(reverse = True)
    card_count = tuple(card_count)
    assert(card_count in hand_score_dict)
    return hand_score_dict[card_count]

def get_hand_sort_value(hand: (str, str)) -> bool:
    # Let the hand score be an integer, and let every card add a power of (1/13) after that
    score = get_hand_score(hand[0])
    quote = 1
    for c in hand[0]:
        quote /= 13
        assert(c in card_score_dict)
        score += quote * card_score_dict[c]
    return score
    


def part_1():
    if USE_TEST_DATA:
        input_list = TEST_DATA.splitlines()
    else:
        input_list = aocd.get_data(day=7).splitlines()

    hands = []
    for line in input_list:
        hands.append(tuple(line.split(" ")))
    
    # Sort from bad to good
    hands.sort(key=get_hand_sort_value)
    total_winnings = 0
    for (idx, hand) in enumerate(hands):
        total_winnings += (idx + 1) * int(hand[1])
    print(total_winnings)


part_1()