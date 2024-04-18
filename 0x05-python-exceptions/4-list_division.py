#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            if isinstance(my_list_1[i], int) or isinstance(my_list_1[i], float):
                if isinstance(my_list_2[i], int) or isinstance(my_list_2[i], float):
                    result_list[i] = my_list_1[i] / my_list_2[i]
    except DivisionByZeroError:
        print("division by 0")
    except IndexError:
        print("out of range")
    finally:
        return result_list
