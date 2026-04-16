# _*_ coding : utf-8 _*_
# @Time : 2026/4/1613:58
# @Author : WuAsia
# @File : data_compare.py
# @Project : PythonProject1

import urllib.request
import gzip
from io import BytesIO
from bs4 import BeautifulSoup
import pandas as pd

# 1. 配置榜单与请求头
TOPTEN_URL = "https://my.jjwxc.net/topten.php?orderstr=12"  # 收入金榜，可改 orderstr
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

# 2. 获取并解压页面
def fetch_page(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
    # 自动解压 gzip
    try:
        data = gzip.decompress(data)
    except:
        pass
    return data.decode("gb18030")  # 晋江编码为 GB18030

# 3. 解析榜单数据
def parse_topten(html):
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", class_="cytable")  # 榜单核心表格
    if not table:
        return []
    rows = table.find_all("tr")[1:]  # 跳过表头
    results = []
    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 8:
            continue
        results.append({
            "排名": cols[0].text.strip(),
            "作品名": cols[1].a.text.strip() if cols[1].a else "",
            "作品链接": f"https://www.jjwxc.net{cols[1].a['href']}" if cols[1].a else "",
            "作者": cols[2].a.text.strip() if cols[2].a else "",
            "作者链接": f"https://www.jjwxc.net{cols[2].a['href']}" if cols[2].a else "",
            "类型": cols[3].text.strip(),
            "风格": cols[4].text.strip(),
            "进度": cols[5].text.strip(),
            "字数": cols[6].text.strip(),
            "积分": cols[7].text.strip()
        })
    return results

# 4. 主流程：爬取 → 解析 → 保存
if __name__ == "__main__":
    html = fetch_page(TOPTEN_URL)
    data = parse_topten(html)
    if data:
        df = pd.DataFrame(data)
        print(df.head())  # 打印前5条
        df.to_excel("晋江收入金榜.xlsx", index=False)  # 保存为 Excel
        print("数据已保存至 晋江收入金榜.xlsx")
    else:
        print("未获取到数据")