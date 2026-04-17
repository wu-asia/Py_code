# _*_ coding : utf-8 _*_
# @Time : 2026/4/1722:53
# @Author : WuAsia
# @File : kfc.py
# @Project : PythonProject1

import urllib.request
import urllib.parse
def create_request(page):
    base_url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=name'
    data = {
        'cname' :'北京',
        'pid' :'',
        'pageIndex':page,
        'pageSize': '10'
    }
    data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {'user-agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}
    request = urllib.request.Request(url=base_url, headers=headers,data=data)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

import json
def down_load(content, page):
    data = json.loads(content)
    with open('kfc_' + str(page) + '.json', mode='w', encoding='utf-8') as f:
        json.dump(data, fp=f, ensure_ascii=False, indent=4)


#base_url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=name'


if __name__ == "__main__":
    start_page = int(input('input start number:'))
    end_page = int(input('input end number:'))

    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        down_load(content, page)