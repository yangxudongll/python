import tkinter
import json
import requests

master=tkinter.Tk()
master.geometry('680x100+500+500')
master.title('有道翻译')

def translating():
    content=entry1.get()
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data={
        'i':content,
        'doctype': 'json'
    }
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    result=requests.post(url,data=data,headers=headers).content.decode()
    ret=json.loads(result)
    response=ret['translateResult'][0][0]['tgt']
    var.set(response)


tkinter.Label(master,text="输入",font={"宋体",18},fg='blue').grid(row=0,column=1)
tkinter.Label(master,text="结果",font={"宋体",18},fg='blue').grid(row=1,column=1)
button1=tkinter.Button(master,text="翻译",font={"宋体",18},command=translating)
button1.grid(row=2,column=1,sticky='W')
buttton2=tkinter.Button(master,text="退出",font={"宋体",18},command=master.quit)
buttton2.grid(row=2,column=2,sticky='E')
entry1=tkinter.Entry(master,width=60,font={"宋体",18})
entry1.grid(row=0,column=2)

var=tkinter.StringVar()
entry2=tkinter.Entry(master,width=60,font={"宋体",18},textvariable=var)
entry2.grid(row=1,column=2)




master.mainloop()