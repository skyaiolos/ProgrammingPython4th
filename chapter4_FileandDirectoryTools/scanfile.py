
"""
    Description:
    File Scanners
Before we leave our file tools survey, it’s time for something that performs a more
tangible task and illustrates some of what we’ve learned so far. Unlike some shell-tool
languages, Python doesn’t have an implicit file-scanning loop procedure, but it’s simple
to write a general one that we can reuse for all time. The module in Example 4-1 defines
a general file-scanning routine, which simply applies a passed-in Python function to
each line in an external file.
"""

def scanner(name, function):
    file = open(name, 'r')  # create a file object
    while True:
        line = file.readline()  # call file methods
        if not line: break  # until end-of-file
        function(line)  # call a function object
    file.close()


"""
def scanner(name, function):
    for line in open(name, 'r'):         # scan line by line
        function(line)                   # call a function object
"""

"""
def scanner(name, function):
    [function(line) for line in open(name, 'r')]
"""
