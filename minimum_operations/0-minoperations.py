#!/usr/bin/python3
"""
Minimum Operations

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0

"""


def minOperations(n):
    if n < 2:
        return 0

    current_num_of_h = 1
    copied = 0
    num_of_operations = 0

    while current_num_of_h < n:
        if n % current_num_of_h == 0:
            copied = current_num_of_h
            num_of_operations += 1

        current_num_of_h += copied
        num_of_operations += 1
    return num_of_operations
