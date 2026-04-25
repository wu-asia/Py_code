# _*_ coding : utf-8 _*_
# @Time : 2026/4/2223:50
# @Author : WuAsia
# @File : npy.py
# @Project : PythonProject1
from ctypes import string_at

#https://sc.chinaz.com/tupian/qinglvtupian.html
#https://sc.chinaz.com/tupian/qinglvtupian_page.html

import urllib.request
from lxml import etree
def create_request(url_string:str, page:int):
    if page == 1:
        url = url_string + '.html'
    else:
        url = url_string + '_' + str(page) + '.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content):
#下载图片
#urllib.reqeust.urlretrieve('图片地址', '文件名称')
    tree = etree.HTML(content)
    tree.xpath()
if __name__ == '__main__':
    url_string = 'https://sc.chinaz.com/tupian/qinglvtupian'
    start_page = int(input('start page:'))
    end_page = int(input('end page:'))
    for page in range(start_page, end_page + 1):
        request = create_request(url_string, page)
        content = get_content(request)
        down_load(content)