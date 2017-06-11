"""
#  Script Description:


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/6/11
from io import BytesIO

stream = BytesIO()
stream.write(b'spam')
print(stream.getvalue())
# b'spam'
stream = BytesIO(b'dpam')
print(stream.read())
# b'spam'
