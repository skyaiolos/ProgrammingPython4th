"""
#  Script Description:


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/6/11
from io import StringIO

buff = StringIO()
print(42, file=buff)
print('spam', file=buff)
print(buff.getvalue())
from PP4E.System.chapter3_ScriptExectionContext.redirect import Output

buff = Output()
print(43, file=buff)
print('eggs', file=buff)
print(buff.text)
