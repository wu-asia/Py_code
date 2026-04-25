# _*_ coding : utf-8 _*_
# @Time : 2026/4/1809:26
# @Author : WuAsia
# @File : urllib_error.py
# @Project : PythonProject1

import urllib.request


url = 'https://blog.csdn.net/sulixu/article/details/119818949'

headers = {'user-agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}

try:
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)

except Exception as e:
    print(e)




