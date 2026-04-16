# _*_ coding : utf-8 _*_
# @Time : 2026/4/1613:55
# @Author : WuAsia
# @File : improve.py
# @Project : PythonProject1

# _*_ coding : utf-8 _*_
# @Time : 2026/4/16 13:49
# @Author : WuAsia
# @File : sjin.py
# @Project : PythonProject1

import urllib.request
import gzip
from io import BytesIO

url = 'https://www.jjwxc.net'

headers = \
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept-Encoding': 'gzip, deflate',  # 允许压缩
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)

data = response.read()
try:
    data = gzip.decompress(data)
except:
    pass

content = data.decode('gb18030')
print(content)
