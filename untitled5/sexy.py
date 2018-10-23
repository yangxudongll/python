# ！user/bin/env python
#---encoding utf-8---
#  author:xudong   time:2018/9/1

import requests
import re
import time
from multiprocessing import Pool
names=[]
urls = []

def get_info():
    pattern1=re.compile('<a href="/song\?id=(.*?)">')
    pattern2=re.compile('<a href="/song\?id=.*?">(.*?)</a></li>')
    with open('D:\爬虫图片\抖音.txt','r') as file:
        data=file.read()
    ids=re.findall(pattern1,data)
    print(ids)
    name=re.findall(pattern2,data)
    for i in name:
        names.append(i)
    url='http://music.163.com/song/media/outer/url?id='
    for i in ids:
        temp=url+str(i)
        urls.append(temp)


def download(url,name):
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    try:
        data=requests.get(url,headers=headers)
        with open('D:\爬虫图片\douyin\{}.mp3'.format(name),'wb') as file:
            file.write(data.content)
            print('正在下载{}'.format(name))
    except:
        pass

def main():
    get_info()
    print(names)
    print(urls)
    pool = Pool(20)
    for i in range(100):
        pool.apply_async(download, (urls[i],names[i]))
    pool.close()
    pool.join()

if __name__=="__main__":
    main()