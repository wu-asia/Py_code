# _*_ coding : utf-8 _*_
# @Time : 2026/4/261:56
# @Author : WuAsia
# @File : url_params.py
# @Project : Project6


import requests

url = 'https://movie.douban.com/j/chart/top_list'

params = {
'type':'24',
'interval_id':'100:90',
'action':'',
'start':'20',
'limit':'20'
}

headers = {
'user-agent' :
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
}

resp = requests.get(url=url,params=params,headers=headers)

resp.encoding = 'utf-8'

print(resp.text)
print(resp.json())



