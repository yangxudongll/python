# ！user/bin/env python
#---encoding utf-8---
#  author:xudong   time:2018/8/28
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
from selenium import webdriver
import re
import requests


chrome_options=Options()
chrome_options.add_argument("--headless")
driver=webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://www.taobao.com')
wait=WebDriverWait(driver,10)
#driver.maximize_window()
input=driver.find_element_by_id('q')
input.send_keys('成人用品')
input.send_keys(Keys.RETURN)
pattern=re.compile('class="J_ItemPic img" src="(.*?)" data-src=')

def next_page(page_number):
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        input.clear()     #清除框内内容
        input.send_keys(page_number)
        submit.click()
    except TimeoutError:
        next_page(page_number)
urls=[]
n=0
def main():
    global n
    for i in range(2,20):
        data = driver.page_source
        htmls=re.findall(pattern,data)
        for html in htmls:
            url="http:"+html
            data=requests.get(url)
            with open('D://性爱//%s.jpg'%str(n),'wb') as file:
                file.write(data.content)
            n+=1
        next_page(i)



if __name__=="__main__":
    main()
driver.quit()
"""

def temp(i):
    url='https://vip.okokbo.com/20180105/wYpEBYN4/800kb/hls/AGLy5540%03d.ts'%i
    r=requests.get(url)
    print(url)
    f=open('./mp4/{}'.format(url[-10:],'ab'))
    f.write()
    f.close()


if __name__=='__main__':
    pool=Pool(20)
    for i in range(6500):
        pool.apply_async(temp,(i,))

    pool.close()
    pool.join()
"""
copy /b .ts *abc.mp4