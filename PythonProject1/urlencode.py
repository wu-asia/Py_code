# _*_ coding : utf-8 _*_
# @Time : 2026/4/1617:01
# @Author : WuAsia
# @File : urlencode.py
# @Project : PythonProject1
from urlib import response

#urlencode 应用场景：多个参数的时候

#https://www.baidu.com/s?wd=周杰伦&sex=男
string_headers='''
accept
image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
accept-encoding
gzip, deflate, br, zstd
accept-language
zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
connection
keep-alive
cookie
BIDUPSID=8CEF1B35D16586F17562AAB86946614D; PSTM=1769332620; BAIDUID=8A9248CBA2CD193B19E32D5350D085DE:FG=1; BAIDUID_BFESS=8A9248CBA2CD193B19E32D5350D085DE:FG=1; ZFY=79jdeIfnhShKr0pTkGUFv6WCnugqZXzwI8Gl2AqYAXM:C; __bid_n=19c70cbf45b115255305b5; BDUSS=c5UzVCYXdQZkhHcVRpVG9DLUNYUGdlcjMwV35Pc0p3LTJibWJDbDVwUjg3TUJwSVFBQUFBJCQAAAAAAAAAAAEAAAC~cRhjzuK549Lmd2d5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHxfmWl8X5lpNH; BDUSS_BFESS=c5UzVCYXdQZkhHcVRpVG9DLUNYUGdlcjMwV35Pc0p3LTJibWJDbDVwUjg3TUJwSVFBQUFBJCQAAAAAAAAAAAEAAAC~cRhjzuK549Lmd2d5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHxfmWl8X5lpNH; BA_HECTOR=8ka42l00aha58k2g2l050k2k248k801ktuo7s26; delPer=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=5; H_PS_PSSID=63144_67861_68165_68263_68296_68370_68420_68541_68546_68516_68621_68613_68676_68690_68737_68796_68880_68908_68834_68927_68995_69003_69012_69017_69024_69014_69052_69070_69036_69083_69163_69188_69205_69214_69243_69227_69241_69230_69234_69248_69291_68779_69251_69252_69254_69257_69258; H_WISE_SIDS=63144_67861_68165_68263_68296_68370_68420_68541_68546_68516_68621_68613_68676_68690_68737_68796_68880_68908_68834_68927_68995_69003_69012_69017_69024_69014_69052_69070_69036_69083_69163_69188_69205_69214_69243_69227_69241_69230_69234_69248_69291_68779_69251_69252_69254_69257_69258
host
mbd.baidu.com
referer
https://www.baidu.com/
sec-ch-ua
"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"
sec-ch-ua-mobile
?0
sec-ch-ua-platform
"Windows"
sec-fetch-dest
image
sec-fetch-mode
no-cors
sec-fetch-site
same-site
user-agent
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36
'''

tmp = string_headers.strip().split('\n')
#print(type(tmp))
d = {}
for i in range(0, len(tmp), 2):
    key = tmp[i]
    value = tmp[i + 1]
    d[key] = value

print(d)

import urllib.parse

data = {'wd' : '周杰伦', 'sex': '男'}

new_data = urllib.parse.urlencode(data)

print(new_data)

base = 'https://www.baidu.com/s?'

url = base + new_data

print(url)

import urllib.request

request = urllib.request.Request(url=url, headers=d)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)


