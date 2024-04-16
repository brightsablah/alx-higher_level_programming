#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is "":
        first_char = None
        length = 0
        return_tuple = (len(sentence), None)
        return return_tuple
    else:
        first_char = sentence[0]
        length = len(sentence)
        return_tuple = (length, first_char)
        return return_tuple
