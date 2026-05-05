# _*_ coding : utf-8 _*_
# @Time : 2026/4/261:28
# @Author : WuAsia
# @File : url_search
# @Project : Project6

import requests

content = input('input the content which you want to search')
url = f'https://www.sogou.com/web?query={content}'

headers = {
'user-agent' :
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
}

resp = requests.get(url=url, headers=headers)

#print(resp.text)
print(resp.request.headers)

print(type(resp.request.headers))











