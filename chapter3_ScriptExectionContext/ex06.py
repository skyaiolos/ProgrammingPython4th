"""
#  Script Description:


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/6/11
import os

pipe = os.popen('Python hello-out.py')          # 'r' is default--read stdout
print(pipe.read())

print(pipe.close())                             # exit status: None is good
