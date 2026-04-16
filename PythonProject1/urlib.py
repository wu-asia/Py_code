# _*_ conding : utf-8 _*_
# @Time : 2026/4/1517:24
# @Author : WuAsia
# @File : urlib.py
# @Project : PythonProject1

#(1) 使用urlib获取网页数据
import urllib.request
#定义一个url 就是要访问的地址

url = 'http://www.baidu.com'

#(2) 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)
#(3) 获取响应的页面的原码
#read 方法  返回的是字节形式的二进制数据
#将二进制数据转换为字符串
#二进制 -> 字符串 解码 decode('编码的形式')
content = response.read().decode('utf-8')
#(4) 打印内容
print(content)



