#!/usr/local/bin/python

""" 
    Example 4-2 is a client script that does simple line translations
"""
from sys import argv


# from PP4E.System.chapter4_FileandDirectoryTools.scanfile import scanner
# from .scanfile import *


class UnknownCommand(Exception): pass


def scanner(name, function):
    file = open(name, 'r')  # create a file object
    while True:
        line = file.readline()  # call file methods
        if not line: break  # until end-of-file
        function(line)  # call a function object
    file.close()


def processLine(line):  # define a function
    if line[0] == '*':  # applied to each line
        print("Ms.", line[1:-1])
    elif line[0] == '+':
        print("Mr.", line[1:-1])  # strip first and last char: \n
    else:
        raise UnknownCommand(line)  # raise an exception


filename = 'data.txt'
if len(argv) == 2: filename = argv[1]  # allow filename cmd arg
scanner(filename, processLine)  # start the scanner

"""
commands = {'*': 'Ms.', '+': 'Mr.'}     # data is easier to expand than code?

def processLine(line):
    try:
        print(commands[line[0]], line[1:-1])
    except KeyError:
        raise UnknownCommand(line)

scanner(argv[1], processLine)
"""
# Ms. Granny
# Mr. Jethro
# Ms. Elly May
# Mr. "Uncle Jed"
