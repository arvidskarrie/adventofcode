
import os
os.environ["AOC_SESSION"] = "53616c7465645f5f9cd071425b0d21d57535630a0d32e44bb5c7fe32070a07aa9170e67bb82f54f3bb900290fd1cb879c94a1e1230f809a51bec010d7f706512"
import aocd
import re
import math
import collections
import itertools


def part_1():
    matrix = [
        [1, 2, 0, 4],
        [5, 6, 7, 8],
        [9, 0, 11, 12]
    ]

    new_matrix = [
        [matrix[x][y]
        for x in range(3)]
        for y in range(4)
    ]

    filtered_matrix = [
        column for column in new_matrix if 0 not in column
    ]

    mixed_strings = ["Hello", "1234", "World", "Python3", "Data1"]

    alphabetical_strings = [s for s in mixed_strings if s.isalpha()]
    converted_strings = [
            "".join([alpha_string[c].upper()
            for c in range(len(alpha_string) - 1, -1, -1)])
            for alpha_string in alphabetical_strings]
    
    products = [
        {"name": "Laptop", "category": "Electronics", "price": 800, "in_stock": True},
        {"name": "TV", "category": "Electronics", "price": 1200, "in_stock": False},
        {"name": "Blender", "category": "Home Appliances", "price": 150, "in_stock": True},
        {"name": "Headphones", "category": "Electronics", "price": 100, "in_stock": True},
        {"name": "Fridge", "category": "Home Appliances", "price": 500, "in_stock": True}
    ]

    electronics_list = [
        product
        for product in products if product["category"] == "Electronics" and product["in_stock"]
    ]

    average_cost = (1 / len(electronics_list)) * sum([
        product["price"]
        for product in electronics_list
    ])

    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    B = [
        [7, 8, 13, 23,],
        [9, 10, 14, 24,],
        [11, 12, 15, 25,],
    ]

    assert len(A[0]) == len(B)

    product = [
        [
            sum([A[row_a][col_a] * B[col_a][col_b] for col_a in range(len(A[0]))])
            for col_b in range(len(B[0]))
        ]
        for row_a in range(len(A))
    ]

    for line in product:
        print(line)


part_1()