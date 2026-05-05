# _*_ coding : utf-8 _*_
# @Time : 2026/4/261:17
# @Author : WuAsia
# @File : my_req.py
# @Project : PythonProject1

import requests

url = 'http://www.baidu.com'

request = requests.get(url)

print(request)

