# _*_ coding : utf-8 _*_
# @Time : 2026/4/1615:07
# @Author : WuAsia
# @File : 晋江文学AU.py
# @Project : PythonProject1

if __name__ == '__main__':

    string_headers = '''
    :authority
    www.jjwxc.net
    :method
    GET
    :path
    /
    :scheme
    https
    accept
    text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
    accept-encoding
    gzip, deflate, br, zstd
    accept-language
    zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
    cache-control
    max-age=0
    cookie
    testcookie=yes; Hm_lvt_bc3b748c21fe5cf393d26c12b2c38d99=1776318737; HMACCOUNT=46178907C68D99FA; timeOffset_o=1150.199951171875; smidV2=2026041613521824e130d074d11002e546d2affe731f01004eb66ac4f042500; JJSESS=%7B%22clicktype%22%3A%22%22%7D; Hm_lpvt_bc3b748c21fe5cf393d26c12b2c38d99=1776318965; JJEVER=%7B%22shumeideviceId%22%3A%22WHJMrwNw1k/EWJ0ZtEcbN3s8EUY4Ad+FtsqFbjLoO0d//T+ZgMqemRr+1snIm/NgSLQDUN2ubU9z6XIsZBkBVTRLMVLTU1VzgdCW1tldyDzmQI99+chXEilO2NpJeo3hh9lCUKKcsmkR3KAhq3N/faTYmmmXo8LlTkQE5YcNLqNriNYPfoOP/bvyfRwmjRN/jFRRuSg/X1FURTkAd7H/eWrNTWLUcBy9vg6PstI534Wr7EQbqbxUARczBSykKSzAgfUGgIqCuSLQ%3D1487582755342%22%7D
    if-modified-since
    Wed, 15 Apr 2026 17:30:06 GMT
    if-none-match
    W/"69dfcb1e-119b0"
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
    Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'''

    tmp = string_headers.strip().split('\n')
    print(tmp)

    lst = []
    for line in tmp:
        line = line.strip()
        if line:
            lst.append(line)

    headers = {}

    for i in range(0, len(lst), 2):
        key = lst[i]
        value = lst[i + 1]
        headers[key] = value

    for k in list(headers.keys()):
        if k.startswith(':'):
            del headers[k]

    print(headers)
