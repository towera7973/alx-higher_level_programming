#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples."""
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            '''appending a 0 if it has one element alreday '''
            tuple_a = tuple_a[0], 0
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
