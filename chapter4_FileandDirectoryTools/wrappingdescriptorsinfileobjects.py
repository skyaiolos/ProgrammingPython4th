__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/18
"""
    Description:
      Wrapping descriptors in file objects
We saw earlier how to go from file object to field descriptor with the  fileno file object
method; given a descriptor, we can use  os module tools for lower-level file access to
the underlying file. We can also go the other way—the  os.fdopen call wraps a file de-
scriptor in a file object. Because conversions work both ways, we can generally use
either tool set—file object or  os module:  
"""
import os

fd_file = os.open(r'.\spam.txt', (os.O_RDWR | os.O_BINARY))
print(fd_file)
# 3

object = os.fdopen(fd_file, 'rb')
print(object.read())
# b'jello stdio file\r\nHello description file\n'