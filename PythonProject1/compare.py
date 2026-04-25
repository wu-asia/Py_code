# _*_ coding : utf-8 _*_
# @Time : 2026/4/2223:16
# @Author : WuAsia
# @File : compare.py
# @Project : PythonProject1


#https://fanqienovel.com/api/author/library/book_list/v0/?page_count=18&page_index=1&gender=-1&category_id=-1&creation_status=-1&word_count=-1&book_type=-1&sort=0&msToken=Bnt-Akn7Az2I7YEJD-wEOs6bVw9UwEUgQ_vwAVETGt2eXRx0tm9vVxB_SKm0sBV3F9w1CeKdknHEQOhknz1_jVdpcoEt0V3jSoAgW_jw5klGZ15WrBpdnA%3D%3D&a_bogus=O7MmgOgEMsm15jVbo7kz970mPB60YW5mgZEPWOQEStoK
#https://fanqienovel.com/api/author/library/book_list/v0/?page_count=18&page_index=0&gender=-1&category_id=-1&creation_status=-1&word_count=-1&book_type=-1&sort=0&msToken=Bnt-Akn7Az2I7YEJD-wEOs6bVw9UwEUgQ_vwAVETGt2eXRx0tm9vVxB_SKm0sBV3F9w1CeKdknHEQOhknz1_jVdpcoEt0V3jSoAgW_jw5klGZ15WrBpdnA%3D%3D&a_bogus=Y7BEkOgEMsm1cEVbo7kz9ttmPmL0YW5dgZEPWOQWczoj
#https://fanqienovel.com/api/author/library/book_list/v0/?page_count=18&page_index=1&gender=-1&category_id=-1&creation_status=-1&word_count=-1&book_type=-1&sort=0&msToken=Bnt-Akn7Az2I7YEJD-wEOs6bVw9UwEUgQ_vwAVETGt2eXRx0tm9vVxB_SKm0sBV3F9w1CeKdknHEQOhknz1_jVdpcoEt0V3jSoAgW_jw5klGZ15WrBpdnA%3D%3D&a_bogus=YvUDhcgEMsm15jVboXkz970mPpE0YW-kgZEPWODzz0oE

import requests
from bs4 import BeautifulSoup

# 你要爬的页面
url = "https://fanqienovel.com/library/all/page_3?sort=hottes"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://fanqienovel.com/"
}

# 发送请求
resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, "html.parser")

# 存储结果
book_list = []

# 提取所有小说卡片
items = soup.find_all("div", class_="novel-item")

if not items:
    print("页面无数据（PC 端此链接仅引导下载 App）")
else:
    for item in items:
        # 书名
        title = item.find("div", class_="novel-title").get_text(strip=True) if item.find("div", class_="novel-title") else "无"
        # 作者
        author = item.find("div", class_="author").get_text(strip=True) if item.find("div", class_="author") else "无"
        # 分类
        category = item.find("div", class_="category").get_text(strip=True) if item.find("div", class_="category") else "无"
        # 简介
        intro = item.find("div", class_="intro").get_text(strip=True) if item.find("div", class_="intro") else "无"

        book_list.append({
            "书名": title,
            "作者": author,
            "分类": category,
            "简介": intro
        })

# 输出结果
print("=" * 50)
print(f"共爬取到 {len(book_list)} 本小说")
print("=" * 50)

for i, book in enumerate(book_list, 1):
    print(f"\n【第{i}本】")
    print(f"书名：{book['书名']}")
    print(f"作者：{book['作者']}")
    print(f"分类：{book['分类']}")
    print(f"简介：{book['简介']}")