# _*_ coding : utf-8 _*_
# @Time : 2026/4/1614:22
# @Author : WuAsia
# @File : rec.py
# @Project : PythonProject1


import urllib.request

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

print(content)
