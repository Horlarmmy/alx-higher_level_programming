#!/usr/bin/python3
"""
Module 0-add_integer
Function add_integer
"""


def add_integer(a, b=98):
    """
    Args:
        a: first number
        b: second number
    Raises:
        TypeError: if a or b is not an integer or float
    Returns:
        the sum of the two numbers
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    sum = a + b
    return sum
