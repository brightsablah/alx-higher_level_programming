#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    copy_string = list(my_string)
    if my_string is not None:
        for char in copy_string:
            if char == 'c':
                copy_string.remove('c')
            if char == 'C':
                copy_string.remove('C')
        return new_string.join(copy_string)
