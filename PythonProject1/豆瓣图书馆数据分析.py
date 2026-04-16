# -*- coding: utf-8 -*-
import requests
import plotly.express as px
from bs4 import BeautifulSoup
import time
import plotly.io as pio

# 让 Plotly 在浏览器打开，体验最流畅
pio.renderers.default = "browser"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

book_data = []

score_count = {
    "9.5分以上": 0,
    "9.0 ~ 9.4分": 0,
    "8.5 ~ 8.9分": 0,
    "8.0 ~ 8.4分": 0,
    "7.5 ~ 7.9分": 0,
    "7.0 ~ 7.4分": 0,
    "6.5 ~ 6.9分": 0,
    "6.5分以下": 0
}

print("正在爬取 豆瓣图书 Top250...\n")

for page in range(0, 10):
    url = f"https://book.douban.com/top250?start={page*25}"
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")

    items = soup.find_all("tr", class_="item")
    for item in items:
        title = item.find("div", class_="pl2").a.get_text(strip=True).replace("\n", "")
        score = float(item.find("span", class_="rating_nums").text)
        info = item.find("p", class_="pl").text

        book_data.append({"书名": title, "评分": score, "信息": info})

        s = score
        if s >= 9.5:
            score_count["9.5分以上"] += 1
        elif 9.0 <= s <= 9.4:
            score_count["9.0 ~ 9.4分"] += 1
        elif 8.5 <= s <= 8.9:
            score_count["8.5 ~ 8.9分"] += 1
        elif 8.0 <= s <= 8.4:
            score_count["8.0 ~ 8.4分"] += 1
        elif 7.5 <= s <= 7.9:
            score_count["7.5 ~ 7.9分"] += 1
        elif 7.0 <= s <= 7.4:
            score_count["7.0 ~ 7.4分"] += 1
        elif 6.5 <= s <= 6.9:
            score_count["6.5 ~ 6.9分"] += 1
        else:
            score_count["6.5分以下"] += 1

    time.sleep(1)
    print(f"第 {page+1} 页完成")

print("\n  爬取完成！共：", len(book_data), "本图书")
print("\n  评分分布：")
for k, v in score_count.items():
    print(f"{k}：{v} 本")

# ==========================
#   图1：交互式圆环饼图
# ==========================
categories = list(score_count.keys())
counts = list(score_count.values())

fig_pie = px.pie(
    names=categories,
    values=counts,
    title="  豆瓣图书 Top250 评分分布（圆环图）",
    hole=0.3,
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig_pie.update_traces(
    textposition="inside",
    textinfo="percent+label",
    hovertemplate="<b>%{label}</b><br>数量：%{value} 本<br>占比：%{percent}"
)

# ==========================
#  图2：交互式柱状图（你要的新增！）
# ==========================
fig_bar = px.bar(
    x=categories,
    y=counts,
    title="  各评分区间图书数量对比（柱状图）",
    labels={"x": "评分区间", "y": "图书数量"},
    color=categories,
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig_bar.update_traces(
    hovertemplate="评分：%{x}<br>数量：%{y} 本"
)

# ==========================
#  展示两个图表（都可交互！）
# ==========================
fig_pie.show()
fig_bar.show()