# _*_ coding : utf-8 _*_
# @Time : 2026/4/1521:32
# @Author : WuAsia
# @File : urllib_download.py
# @Project : PythonProject1

import urllib.request

#下载网页
# url_page = 'http://www.baidu.com'
# urllib.request.urlretrieve(url=url_page, filename='baidu.html')

#下载图片
url_photo = 'https://ts1.tc.mm.bing.net/th/id/R-C.2fc944004f64dd0682f5e4fddca9a3bd?rik=aoU7kH4yvU6DDA&riu=http%3a%2f%2fn.sinaimg.cn%2fsinakd10022%2f268%2fw641h427%2f20211018%2fe60d-6cc369c3b671d6d340ef69cdd454387b.jpg&ehk=MzGdhVOxQvhnoPrBKEV63sWo2VsXGrxxh1DRcXuZewM%3d&risl=&pid=ImgRaw&r=0'
urllib.request.urlretrieve(url=url_photo, filename='photo1.jpg')

#下载视频