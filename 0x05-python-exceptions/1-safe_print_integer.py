#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer with "{:d}".format(). which means its an integer only 

    Argments :
        value: The integer to print.Could not be an integer so it will bring an error 

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
