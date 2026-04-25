# _*_ coding : utf-8 _*_
# @Time : 2026/4/1807:09
# @Author : WuAsia
# @File : xpath.py
# @Project : PythonProject1

from lxml import etree

#xpath解析
#(1) 本地文件
#(2) 服务器响应文件 response.read().decode('utf-8') *****

tree = etree.parse('xpath.html')
#li_list = tree.xpath('//body//ul/li')
# 查找ul下面的li
#li_list = tree.xpath('//ul/li[@id="l2"]/text()')
li_list1 = tree.xpath('//ul/li[@id="l1"]/@class')
#li_list = tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')
li_list = tree.xpath('//ul/li[@id="l1" or @id="l2"]/text()')
print(li_list)
print(len(li_list))
#print(li_list1)
