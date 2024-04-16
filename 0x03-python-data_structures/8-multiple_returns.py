#!/usr/bin/python3
def multiple_returns(sentence):
    return_tup = ()
    if sentence is "":
        first_char = None
        return_tuple = (len(list(sentence)), first_char)
        return return_tuple
    else:
        first_char = sentence[0]
        return_tuple = (len(list(sentence)), first_char)
        return return_tuple
