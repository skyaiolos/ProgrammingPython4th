__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/19
"""
    Description:
        Other os module file tools
The  os module also includes an assortment of file tools that accept a file pathname
string and accomplish file-related tasks such as renaming ( os.rename ), deleting
( os.remove ), and changing the file’s owner and permission settings ( os.chown ,
os.chmod ). Let’s step through a few examples of these tools in action:
"""
import os

os.chmod('spam.txt', 0o777)
os.rename(r'.\spam.txt', r'.\eggs.txt')
os.remove(r'.\spam.txt')
#
# FileNotFoundError: [WinError 2] The system cannot find the file specified: 'spam.txt'

os.remove(r'.\eggs.txt')
