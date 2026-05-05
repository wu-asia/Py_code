# _*_ coding : utf-8 _*_
# @Time : 2026/4/2923:43
# @Author : WuAsia
# @File : url_re.py
# @Project : Project6

import re
from zoneinfo import reset_tzpath

# result = re.findall("a", "我是一个abcdeafg")
# print(result)

# result = re.findall(r"\d*", "我18是一个100000")
# print(result)

# result = re.finditer(r"\d+", "wo18kafj100")
#
# for item in result: #从迭代器中拿到数据
#     print(item.group()) #.group()是将其中的匹配数据拿出来


#search只会匹配到第一次匹配的内容
result = re.search(r"\d+", "我是周杰伦，今年32岁，我是5年4版")
print(result)
































