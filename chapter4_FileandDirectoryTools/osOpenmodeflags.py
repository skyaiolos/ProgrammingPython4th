__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/18
"""
    Description:
        os.open mode flags
So why the extra file tools in  os ? In short, they give more low-level control over file
processing. The built-in  open function is easy to use, but it may be limited by the un-
derlying filesystem that it uses, and it adds extra behavior that we do not want. The
os module lets scripts be more specific—for example, the following opens a descriptor-
based file in read-write and binary modes by performing a binary “or” on two mode
flags exported by  os :
"""
import os

fdfile = os.open(r'.\spam.txt', (os.O_RDWR | os.O_BINARY))
fd_read = os.read(fdfile, 20)
print(fd_read)
# b'Hello stdio file\r\nHe'
print(os.lseek(fdfile, 0, 0))
print(os.read(fdfile, 100))
# b'Hello stdio file\r\nHello description file\n'
print(os.lseek(fdfile, 0, 0))
print(os.write(fdfile, b'HELLO'))
# 0
# 5
