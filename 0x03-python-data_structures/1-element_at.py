#!/usr/bin/python3
def element_at(my_list, idx):
    list_len = len(my_list) - 1
    if idx < 0 or idx > list_len:
        return None
    else:
        print("{}".format(my_list[idx]))
