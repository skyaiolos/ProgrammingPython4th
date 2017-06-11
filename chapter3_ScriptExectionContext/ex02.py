"""
#  Script Description:


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/6/11
from io import StringIO

buff = StringIO()
print(buff.write('spam\n'))

print(buff.write('eggs\n'))

print(buff.getvalue())

buff = StringIO('ham\nspam\n')
print(buff.readline())
print(buff.readline())
print(buff.readline())
