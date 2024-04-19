#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exceptions as e:
        print("Exception: {}").format(e), file=sys.error)
        return None
