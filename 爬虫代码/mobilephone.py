# from selenium import webdriver
# import requests
# import re
# from multiprocessing import Pool
# from selenium.webdriver.common.by import By
# from pyquery import PyQuery as pq
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# names=[]
# ids=[]
#
# url='http://www.baidu.com'
# driver=webdriver.Chrome()
# driver.get(url)
# driver.find_element(By.CSS_SELECTOR,'#kw')
# print('ok')
# time.sleep(20)
#
# driver.quit()
v=[8.214,7.408,6.879,5.490,5.196]
sum=0
for i in v:
    sum=sum+i
average=sum/5
print(average)
U=[1.886,1.752,1.401,0.871,0.671]
sum2=0
for i in U:
    sum2+=i
average2=sum2/5
print(average2)
x=0
for i in range(5):
    x+=v[i]*U[i]
x=x-5*(average**2)
print(x)
y=0
for i in range(5):
    y+=v[i]**2
y=y-5*(average**2)
print(y)
print(x/y)
t=average2-(x/y)*average
print(t)