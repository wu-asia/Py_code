# _*_ coding : utf-8 _*_
# @Time : 2026/4/1622:51
# @Author : WuAsia
# @File : page.py
# @Project : PythonProject1

#https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=0&limit=20
#https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=20&limit=20
#https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
#start=40&limit=20


import urllib.parse
import urllib.request
def creat_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action='
    data = {
        'start': (page - 1) * 20,
    'limit': 20}
    data = urllib.parse.urlencode(data)
    url = base_url + data
    #print(url)
    headers = {'user-agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}
    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

import json
def down_load(content, page):
    content = json.dumps(json.loads(content), ensure_ascii=False, indent=4)
    page = str(page)
    with open('douban_' + page + '.json', mode = 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    import urllib.request
    start_page = int(input('input start number:'))
    end_page = int(input('input end number:'))

    for page in range(start_page, end_page + 1):
        #获取请求
        request = creat_request(page)
        #获取内容
        content = get_content(request)

        down_load(content, page)