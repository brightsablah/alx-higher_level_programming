#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    if my_string is not None:
        for char in list(my_string):
            if char =! 'c' and char =! 'C':
                new_string.append(char)
        return new_string
