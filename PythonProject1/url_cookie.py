# _*_ coding : utf-8 _*_
# @Time : 2026/4/1809:37
# @Author : WuAsia
# @File : url_cookie.py
# @Project : PythonProject1

#使用场景：需要登录的情况
import urllib.request

string_headers = '''
accept
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
accept-encoding
gzip, deflate, br, zstd
accept-language
zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
cache-control
max-age=0
cookie
_T_WM=87bf0ef80a3d6bf7d4492732ad477400; SCF=AjMDiUgGknZD0iRPbehfyasvIcxCjQpHCq2Y8bP41FHVqf3xf1obLxHeT8Xn6YI96zk8A7ddqyynWIEhKW3-ySE.; SUB=_2A25E5pGfDeRhGe5N7FcT8C3LzDyIHXVnnatXrDV6PUJbktAbLULTkW1NdAmFgZ_LCjzF0CjvYp1pNV4TngGX7N9w; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFsxDHS8B9YcqCBVv0VcG2O5NHD95QRe0Mfeo50S0M7Ws4DqcjMi--NiK.Xi-2Ri--ciKnRi-zN1heNSKz7e0MNe5tt; SSOLoginState=1776476623; ALF=1779068623
priority
u=0, i
sec-ch-ua
"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"
sec-ch-ua-mobile
?0
sec-ch-ua-platform
"Windows"
sec-fetch-dest
document
sec-fetch-mode
navigate
sec-fetch-site
none
sec-fetch-user
?1
upgrade-insecure-requests
1
user-agent
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36
'''

tmp = string_headers.strip().split('\n')

headers={}
for i in range(0, len(tmp), 2):
    key=tmp[i]
    value=tmp[i + 1]
    headers[key] = value


url = 'https://weibo.cn/6451491586/info'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    'cookie':'_T_WM=87bf0ef80a3d6bf7d4492732ad477400; SCF=AjMDiUgGknZD0iRPbehfyasvIcxCjQpHCq2Y8bP41FHVqf3xf1obLxHeT8Xn6YI96zk8A7ddqyynWIEhKW3-ySE.; SUB=_2A25E5pGfDeRhGe5N7FcT8C3LzDyIHXVnnatXrDV6PUJbktAbLULTkW1NdAmFgZ_LCjzF0CjvYp1pNV4TngGX7N9w; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFsxDHS8B9YcqCBVv0VcG2O5NHD95QRe0Mfeo50S0M7Ws4DqcjMi--NiK.Xi-2Ri--ciKnRi-zN1heNSKz7e0MNe5tt; SSOLoginState=1776476623; ALF=1779068623',
    'referer'
}
request = urllib.request.Request(url=url,headers=headers)

reponse = urllib.request.urlopen(request)

content = reponse.read().decode('utf-8')

with open('weibo.html', mode='w', encoding='utf-8') as f:
    f.write(content)
