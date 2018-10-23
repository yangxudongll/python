# ！user/bin/env python
#---encoding utf-8---
#  author:xudong   time:2018/9/13
#做一个有界面的网易音乐下载爬虫
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import tkinter
import os

class GetUrl:
    def __init__(self):
        self.urls=[]

    def get_url(self,song):
        link_id='http://music.163.com/song/media/outer/url?id='
        url='https://music.163.com/#/playlist?id=541112925'

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        wait=WebDriverWait(driver,10)
        driver.get(url)
        input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#srch')))
        input.send_keys(song)
        input.send_keys(Keys.RETURN)
        driver.switch_to_frame('contentFrame')
        html=driver.find_element_by_class_name('srchsongst')
        items=html.find_elements(By.CSS_SELECTOR,'.item.f-cb.h-flag')
        print(len(items))
        for item in items:
            try:
                ids=item.find_elements(By.CLASS_NAME,'td')[0].find_element(By.CLASS_NAME,'hd')
                info={
                    'ID':item.find_element(By.CLASS_NAME,'sn').find_element(By.CLASS_NAME,'text').find_element(By.TAG_NAME,'a').get_attribute('href')[30:],
                    'Name':ids.find_element(By.TAG_NAME,'a').get_attribute('data-res-data'),
                    'Author':item.find_element(By.CSS_SELECTOR,'.td.w1').find_element(By.CLASS_NAME,'text').find_element(By.TAG_NAME,'a').text

                }
                self.urls.append(info)
            except:
                pass
        print('ok')
        driver.quit()




class Window_Show:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('400x100')

    def down_show(self):
        song=GetUrl()

        def get_song_name(event):
            song.get_url(entry1.get())
            def download():
                link_id = 'http://music.163.com/song/media/outer/url?id='
                link_id += song.urls[0]['ID']
                data = requests.get(link_id)
                if os.path.isdir('D://网易') == False:
                    os.mkdir('D://网易')
                with open('D://网易//{}.mp3'.format(song.urls[0]['Name']+'_'+song.urls[0]['Author']), 'wb') as file:
                    file.write(data.content)
            label=tkinter.Label(self.root,text=song.urls[0]['Name']+'   '+song.urls[0]['Author'],width=20)
            label.grid(row=2,column=1)
            button=tkinter.Button(self.root,text='下载',command=download,width=5)
            button.grid(row=2,column=2)

        label=tkinter.Label(self.root,text='请输入需要下载的歌曲',width=20)
        label.grid(row=1,column=1)
        entry1=tkinter.Entry(self.root,width=20)
        entry1.grid(row=1,column=2)
        button1=tkinter.Button(self.root,text='搜索',width=5)
        button1.grid(row=1,column=3)

        button1.bind('<Button-1>',get_song_name)

        self.root.mainloop()

def main():
    show=Window_Show()
    show.down_show()


if __name__=="__main__":
    main()

