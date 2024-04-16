#!/usr/bin/python3
def multiple_returns(sentence):
    return_tup = ()
    if sentence is "":
        return_tuple = (len(list(sentence)), None)
    else:
        return_tuple = (len(list(sentence)), list(sentence)[0])
    return return_tuple
