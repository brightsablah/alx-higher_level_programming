#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # extension of tuples to have at least length of 2
    ext_tup_a = tuple_a + (0, 0)[:2 - len(tuple_a)]
    ext_tup_b = tuple_b + (0, 0)[:2 - len(tuple_b)]
    res_tup = (ext_tup_a[0] + ext_tup_b[0], ext_tup_a[1] + ext_tup_b[1])
    return res_tup
