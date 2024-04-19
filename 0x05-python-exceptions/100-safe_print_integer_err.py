#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            raise TypeError
    except (TypeError, ValueError) as e:
        sys.stderr.write("Exception: " + str(e))
        return False
