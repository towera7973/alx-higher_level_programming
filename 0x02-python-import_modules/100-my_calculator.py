#!/usr/bin/python3
'''Proj:Build  Calculator '''
'''Author:Towera Mndoli'''
from sys import exit, argv
from calculator_1 import add, sub, div, mul
if __name__ == "__main__":
    Argcount = len(argv)
    if Argcount != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        op = argv[2]
        a = int(argv[1])
        b = int(argv[3])
        if op== "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif op == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif op== "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif op == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
