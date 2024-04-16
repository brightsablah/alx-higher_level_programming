#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is "":
        first_char = None
        return_tuple = (len(sentence), first_char)
        return return_tuple
    else:
        first_char = sentence[0]
        return_tuple = (len(sentence), first_char)
        return return_tuple
