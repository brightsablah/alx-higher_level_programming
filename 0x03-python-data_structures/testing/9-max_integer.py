#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    largestNum = my_list[0]
    for i in range(len(my_list)):
        if i < len(my_list) and my_list[i] > largestNum:
            largestNum = my_list[i]
    return largestNum
