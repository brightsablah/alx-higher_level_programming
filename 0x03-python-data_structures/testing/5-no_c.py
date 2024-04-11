#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    copy = list(my_string)
    for index in range(len(my_string)):
        if my_string[index] == 'c':
            copy.remove('c')
        if my_string[index] == 'C':
            copy.remove('C')
    return new_string.join(copy)
