#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list) - 1
    while list_len >= 0:
        print("{}".format(my_list.pop))
        list_len -= 1
