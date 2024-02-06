#!/usr/bin/python3
"""defines a test fie reading function """
def read_file(filename=""):
    """function that reads a text file and prints it"""

    with open(filename, encoding="utf-8") as f:
        text = f.read()
        print(text, end="")
