# _*_ coding : utf-8 _*_
# @Time : 2026/4/1622:02
# @Author : WuAsia
# @File : aiax_film.py
# @Project : PythonProject1

import urllib.request
#https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=0&limit=20
#https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=20&limit=20
#https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
#start=40&limit=20
url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
import json
formatted = json.dumps(json.loads(content), ensure_ascii=False, indent=4)
with open('douban.json', 'w', encoding='utf-8') as f:
    f.write(formatted)
