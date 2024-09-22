#!/usr/bin/python3
""" New Module"""


def add_integer(a, b=98):
    if a is not int or a is not float:
        raise TypeError("a must be an integer")
    if b is not int or b is not float:
        raise TypeError("b must be an integer")
    num1 = int(a)
    num2 = int(b)
    sum = num1 + num2
    return sum
