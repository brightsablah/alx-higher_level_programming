#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        for char in my_string:
            if char == 'c' or char == 'C':
                my_string.remove(char)
        return my_string
