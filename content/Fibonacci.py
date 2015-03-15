#!/usr/bin/python3
"""
Fibonacci.py

Provides functions for producing Fibonacci sequences.
"""


def sequence(count):
    if count == 0:
        return ()
    elif count == 1:
        return (0)
    else:
        result = [0,1]
        for num in range(count - 2):
            result.append(result[-1] + result[-2])
        return tuple(result)
