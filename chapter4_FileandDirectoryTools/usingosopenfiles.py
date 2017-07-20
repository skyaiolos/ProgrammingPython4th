__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/18
"""
    Description:
      Using os.open files
To give you the general flavor of this tool set, though, let’s run a few interactive ex-
periments. Although built-in file objects and  os module descriptor files are processed
with distinct tool sets, they are in fact related—the file system used by file objects simply
adds a layer of logic on top of descriptor-based files.
In fact, the  fileno file object method returns the integer descriptor associated with a
built-in file object. For instance, the standard stream file objects have descriptors 0, 1,
and 2; calling the  os.write function to send data to  stdout by descriptor has the same
effect as calling the  sys.stdout.write method  
"""
import sys
import os

for stream in (sys.stdin, sys.stdout, sys.stderr):
    print(stream.fileno())
# 0
# 1
# 2
std = sys.stdout.write("Hello stdio world\n")  # write via file method
print(std)

_os = os.write(1, b"Hello descriptor world\n") # write via os module
print(_os)
