# _*_ coding : utf-8 _*_
# @Time : 2026/4/261:18
# @Author : WuAsia
# @File : my_reru.py
# @Project : Project6


import requests
import json
url = 'http://www.baidu.com'

rep = requests.get(url)
rep.encoding = 'utf-8'
print(rep.text)
# content = rep.text
#
# content = json.dumps(json.loads(content), ensure_ascii=False, indent=4)
#
# print(content)