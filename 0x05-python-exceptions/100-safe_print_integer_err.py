#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print({:d"}.format(value))
            return True
    except TypeError as e:
        sys.stderr.write("Exception: " + str(e))
        return False
