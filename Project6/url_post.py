# _*_ coding : utf-8 _*_
# @Time : 2026/4/261:39
# @Author : WuAsia
# @File : url_post
# @Project : Project6
import requests
import json

url = 'https://fanyi.baidu.com/sug'

data = {
    'kw' : input('input a word：')
}

resp = requests.post(url=url, data=data)

print(resp.json()['data'])









