import requests,time,json,re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class robot(object):
    def __init__(self):
        # chat = input('请输入内容：')
        pass

    def crawl(self,chat):
        url2 = r'https://open.drea.cc/bbsapi/chat/get'
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
        params = {'keyWord': chat,
'userName': 'type=bbs'}
        res = requests.get(url2,headers=headers,params=params)
        self.lists = res.json()
        con = self.lists['data']['reply']
        return con

from tkinter import * #窗口模型
class Application(object):
    def __init__(self):
        self.window = Tk()
        self.fanyi = robot()
        self.window.title(u'聊天机器人')   #Unicode是書寫國際文本的標準方法。如果你想要用非英語寫文本,那麼你需要有一個支持Unicode的編輯器。
                                    #類似地,Python允許你處理Unicode文本——你只需要在字符串前加上前綴u或U。
        #设置窗口大小和位置
        self.window.geometry('310x370+500+300')     # （+） 是指出现在屏幕的位置
        self.window.minsize(310,370)
        self.window.maxsize(310,370)
        #创建一个文本框
        self.result_text1 = Text(self.window,bg='beige')
        self.result_text1.place(x = 10,y = 5,width = 285,height = 152)
        self.result_text1.bind("<Key-Return>",self.submit1)    #回车翻译

        #创建一个按钮
        #为按钮添加事件
        self.submit_btn = Button(self.window,text=u'对话',command = self.submit)
        self.submit_btn.place(x = 205,y = 165,width = 35,height = 25)
        self.submit_btn2 = Button(self.window,text=u'清空',command = self.clean)
        self.submit_btn2.place(x = 250,y = 165,width = 35,height = 25)

        #翻译结果
        self.result_text = Text(self.window,bg='beige')
        self.result_text.place(x=10,y=195,width=285,height=165)

        #翻译结果标题
        self.title_label = Label(self.window,text=u'Smile_robot')
        self.title_label.place(x=10,y=165)

    def submit1(self,event):
        #从输入框获取用户输入的值
        content = self.result_text1.get(0.0,END).strip().replace("\n"," ")
        #把这个值传送给服务器进行翻译

        translate = self.fanyi.crawl(content)
        #将结果显示在窗口中的文本框中

        self.result_text.delete(0.0,END)
        self.result_text.insert(END,translate)     # insert表示在光标选定的位置输入,end表示在最后输入

    def submit(self):
        #从输入框获取用户输入的值
        content = self.result_text1.get(0.0,END).strip().replace("\n"," ")
        #把这个值传送给服务器进行翻译

        translate = self.fanyi.crawl(content)
        #将结果显示在窗口中的文本框中

        self.result_text.delete(0.0,END)
        self.result_text.insert(END,translate)
        print(content)

    def clean(self):
        self.result_text1.delete(0.0,END)
        self.result_text.delete(0.0,END)

    def run(self):
        self.window.mainloop()



if __name__ ==  "__main__":
    app = Application()
    app.run()
