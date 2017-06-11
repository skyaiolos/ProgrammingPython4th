"""
#  Script Description:


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/6/11
from io import StringIO
import sys

buff = StringIO()
temp = sys.stdout
sys.stdout = buff
print(42, 'spam', 3.141)
sys.stdout = temp
print(buff.getvalue())
