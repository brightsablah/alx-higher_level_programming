#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = map(lambda item, number: item * number, my_list)
    return list(new_list)
