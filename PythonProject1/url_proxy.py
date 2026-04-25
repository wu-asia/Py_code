# _*_ coding : utf-8 _*_
# @Time : 2026/4/1814:10
# @Author : WuAsia
# @File : url_proxy.py
# @Project : PythonProject1

import urllib.request

url = 'https://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
}
proxies = {
    
}
handler = urllib.request.ProxyHandler()

opener = urllib.request.build_opener(handler)
response = opener.open(request)

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('proxy.html', mode='w', encoding='utf-8') as f:
    f.write(content)

