__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/18
"""
    Description:
        Because file objects we open explicitly behave the same way, it’s also possible to process
a given real external file on the underlying computer through the built-in  open function,
tools in the  os module, or both (some integer return values are omitted here for brevity):
"""

file = open(r'.\spam.txt', 'w')
file.write("Hello stdio file\n")
file.flush()
fd = file.fileno()
print(fd)
import os

os.write(fd, b'Hello description file\n')
file.close()
