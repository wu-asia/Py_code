# _*_ coding : utf-8 _*_
# @Time : 2026/4/1521:14
# @Author : WuAsia
# @File : one_variable_six_methods.py
# @Project : PythonProject1

import urllib.request

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)

# 一个类型和六种方法
# response是HTTPResponse的类型
# print(type(response))

#按照一个字节一个字节的去读
#content = response.read().decode('utf-8')
content = response.readline()
#print(type(response))
# content1 = response.readlines().encode('utf-8')
print(content)
# print(content1)

print(response.getcode())
print(response.geturl())
print(response.getheaders())

