# _*_ coding : utf-8 _*_
# @Time : 2026/4/1521:57
# @Author : WuAsia
# @File : dating.py
# @Project : PythonProject1

import urllib.request

url = 'https://www.baidu.com'

#url的组成
#http/https     www.baidu.com
#协议                   主机       端口号  路径   参数

headers = {'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}
#因为urlopen方法中不能存储字典 所以headers 不能传递进去
#请求定制对象
#注意 因为参数顺序的问题  不能直接写url 和headers 中间还有data 所以我们需要关键字传参
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
