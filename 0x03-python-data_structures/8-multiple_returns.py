#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        first_char = None
        length = 0
    else:
        first_char = sentence[0]
        length = len(sentence)
    tuple = (length, first_char)
    return tuple
