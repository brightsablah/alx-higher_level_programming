#!/usr/bin/python3
""" New Module"""


def add_integer(a, b=98):
    """ addition function """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    num1 = int(a)
    num2 = int(b)
    sum = num1 + num2
    return sum

print(add_integer(3))