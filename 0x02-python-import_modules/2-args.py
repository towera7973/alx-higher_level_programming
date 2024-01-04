#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    argCount = len(argv) - 1 
    '''counts how many arguments you punch in '''
    if argCount == 0:
        print("{} arguments.". format(argCount))
    elif argCount == 1:
        print("{} argument:".format(argCount))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(argCount))
        loopcount = 1
        for arg in argv[1:]:
            ''' the for loop is endless with arg[1:] open end ,you can put more arguments as you want '''
            print("{}: {}".format(loopcount, arg))
            loopcount += 1
