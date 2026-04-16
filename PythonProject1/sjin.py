# _*_ coding : utf-8 _*_
# @Time : 2026/4/1613:49
# @Author : WuAsia
# @File : sjin.py
# @Project : PythonProject1

import urllib.request

url = 'https://www.jjwxc.net'

response = urllib.request.urlopen(url)

content = response.read().decode('gb18030')

print(content)


