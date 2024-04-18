#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                    if my_list_2[i] == 0:
                        raise ZeroDivisionError
                    result_list.append(my_list_1[i] / my_list_2[i])
                else:
                    raise TypeError
            except ZeroDivisionError:
                print("division by 0")
                result_list.append(0)
            except TypeError:
                print("wrong type")
                result_list.append(0)
    except IndexError:
        print("out of range")
        result_list.append(0)
    finally:
        return result_list
