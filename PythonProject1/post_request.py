# _*_ coding : utf-8 _*_
# @Time : 2026/4/1620:15
# @Author : WuAsia
# @File : post_request.py
# @Project : PythonProject1
#post 请求
import urllib.request
import urllib.parse
url = 'https://fanyi.baidu.com/sug'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}
data = {'kw':'spider'}
data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=url, data=data, headers=headers)

reponse = urllib.request.urlopen(request)

content = reponse.read().decode('utf-8')

print(content)

import json

c = json.loads(content)

print(c)


