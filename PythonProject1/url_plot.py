# _*_ coding : utf-8 _*_
# @Time : 2026/4/1808:05
# @Author : WuAsia
# @File : url_plot.py
# @Project : PythonProject1
import urllib.request
from lxml import etree

#(1)请求对象的定制
#(2)获取网页源码
#(3)下载

#需求，下载前室友的地址
#https://sc.chinaz.com/tupian/qinglvtupian.html
#https://sc.chinaz.com/tupian/qinglvtupian_2.html
#https://sc.chinaz.com/tupian/qinglvtupian_3.html

def create_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_' + str(page) + '.html'
    #print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
    }

    reqeust = urllib.request.Request(url=url, headers=headers)
    return reqeust


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content):
        tree = etree.HTML(content)
        tree.xpath()

if __name__ == '__main__':
    start_page = int(input('start page:'))
    end_page = int(input('end page:'))

    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        down_load(content)