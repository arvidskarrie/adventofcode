
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
    'T': 11,
    '9': 10,
    '8': 9,
    '7': 8,
    '6': 7,
    '5': 6,
    '4': 5,
    '3': 4,
    '2': 3,
    'J': 2,
}

ALL_BUT_J_LIST = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def get_hand_score(hand: str):
    best_score = 0
    for joker_val in ALL_BUT_J_LIST:
        new_hand = hand.replace('J', joker_val)
        card_count = list(collections.Counter(list(new_hand)).values())
        card_count.sort(reverse = True)
        card_count = tuple(card_count)
        assert(card_count in hand_score_dict)
        best_score = max(best_score, hand_score_dict[card_count])
    return best_score

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
        print(hand[0])
    print(total_winnings) # 254833040 too low


part_1()