#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    max_idx = len(my_list) - 1
    if idx < 0:
        return my_list
    elif idx > max_idx:
        return my_list
    else:
        my_list.insert(idx, element)
        return my_list
