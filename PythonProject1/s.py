# _*_ coding : utf-8 _*_
# @Time : 2026/4/1614:45
# @Author : WuAsia
# @File : string.py
# @Project : PythonProject1


if __name__ == '__main__':

    string_headers = '''
    accept
    text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
    accept-encoding
    gzip, deflate, br, zstd
    accept-language
    zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
    cache-control
    max-age=0
    connection
    keep-alive
    cookie
    BIDUPSID=8CEF1B35D16586F17562AAB86946614D; PSTM=1769332620; BAIDUID=8A9248CBA2CD193B19E32D5350D085DE:FG=1; BAIDUID_BFESS=8A9248CBA2CD193B19E32D5350D085DE:FG=1; ZFY=79jdeIfnhShKr0pTkGUFv6WCnugqZXzwI8Gl2AqYAXM:C; __bid_n=19c70cbf45b115255305b5; BDUSS=c5UzVCYXdQZkhHcVRpVG9DLUNYUGdlcjMwV35Pc0p3LTJibWJDbDVwUjg3TUJwSVFBQUFBJCQAAAAAAAAAAAEAAAC~cRhjzuK549Lmd2d5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHxfmWl8X5lpNH; BDUSS_BFESS=c5UzVCYXdQZkhHcVRpVG9DLUNYUGdlcjMwV35Pc0p3LTJibWJDbDVwUjg3TUJwSVFBQUFBJCQAAAAAAAAAAAEAAAC~cRhjzuK549Lmd2d5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHxfmWl8X5lpNH; BD_UPN=12314753; BA_HECTOR=8ka42l00aha58k2g2l050k2k248k801ktuo7s26; delPer=0; BD_CK_SAM=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_WISE_SIDS=63144_67861_68165_68263_68296_68370_68420_68541_68546_68516_68621_68613_68676_68690_68737_68796_68880_68908_68834_68927_68981_68995_69003_69012_69017_69024_69014_69052_69070_69036_69083_69163_69188_69205_69214_69243_69227_69241_69230_69234_69248_69291_68779; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=5; H_PS_PSSID=63144_67861_68165_68263_68296_68370_68420_68541_68546_68516_68621_68613_68676_68690_68737_68796_68880_68908_68834_68927_68981_68995_69003_69012_69017_69024_69014_69052_69070_69036_69083_69163_69188_69205_69214_69243_69227_69241_69230_69234_69248_69291_68779; sugstore=0; SMARTINPUT=%5Bobject%20Object%5D; H_PS_645EC=658fWSfz0NZZ25AkLYtfAXjEagKvjr5OTVON8ZGFLStnRAH4sBY1%2FS5idXs; baikeVisitId=96606701-31a6-4fd8-9fc9-68a9518219be
    host
    www.baidu.com
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

    lst = []
    i = 0
    tmp = string_headers.strip().split('\n')

    for line in tmp:
        if line != ' ':
            lst.append(line)
    print(lst)
    headers = {}
    for i in range(0, len(lst), 2):
        key = lst[i]
        value = lst[i + 1]
        headers[key] = value


    print(headers)



