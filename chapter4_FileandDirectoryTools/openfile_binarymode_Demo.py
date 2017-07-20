__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/18
"""
    Description:
        In this case, binary mode strings  rb+ and  r+b in the basic  open call are equivalent:
"""
file = open(r'.\spam.txt', 'rb+')
fr = file.read(20)
print(fr)
# b'HELLO stdio file\r\nHe'
file.seek(0)
print(file.read(100))
# b'HELLO stdio file\r\nHello description file\n'

file.seek(0)
print(file.write(b'jello'))
# 5
file.seek(0)
print(file.read())
# b'jello stdio file\r\nHello description file\n'