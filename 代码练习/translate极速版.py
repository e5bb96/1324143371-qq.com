'''var r = function(e) {
        var t = n.md5(navigator.appVersion),
        r = "" + (new Date).getTime(),
        i = r + parseInt(10 * Math.random(), 10);
        return {
            ts: r,
            bv: t,
            salt: i,
            sign: n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
        }
    };'''

# var t = “” + ((new Date).getTime() + parseInt(10 * Math.random(),
# 10));
# 这行就是生成一个时间戳，再加进去一个0-10的随机数

# sign: n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
# md5一共需要四个参数，第一个和第四个都是固定的字符串，第三个是所谓的salt。第二个就是输入的要查找的单词

import requests,json,time,random
#hashlib 提供字符加密功能
import hashlib      #摘要算法，如MD5，SHA1
class translates(object):
    def __init__(self):
        pass
    def crawl(self,content):
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        #content = input('请输入要翻译的内容：')
        f = str(int(time.time()*1000)+random.randint(1,10))
        md5 = hashlib.md5()
        md5.update(("fanyideskweb" + content + f + "n%A-rKaT5fb[Gy?;N5@Tj").encode('utf-8'))
        sigh = md5.hexdigest()
        g = str(int(int(f)*0.1))

        data = {
                "i": content,
                "from": "AUTO",
                "to": "AUTO",
                "smartresult": "dict",
                "client": "fanyideskweb",
                "salt": f,
                "sign": sigh,
                "doctype": "json",
                "version": "2.1",
                "keyfrom": "fanyi.web",
                "action": "FY_BY_CLICKBUTTION",
                "typoResult": "false",
            }


        header = '''Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7
Connection: keep-alive
Content-Length: 236
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: OUTFOX_SEARCH_USER_ID=-1081289583@10.108.160.19; OUTFOX_SEARCH_USER_ID_NCOO=822922738.4474599; JSESSIONID=aaasCFUZVdvzt7wwuAa7w; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcqpXsJhPc2RhcieCa7w; _ntes_nnid=c5d1418ce694b7c86e97b16e8457c523,1575186614476; ___rl__test__cookies=1575189494064
Host: fanyi.youdao.com
Origin: http://fanyi.youdao.com
Referer: http://fanyi.youdao.com/
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36
X-Requested-With: XMLHttpRequest'''
        header = dict([line.split(": ",1) for line in header.split("\n")])
        req = requests.post(url,data=data,headers=header)

        js = json.loads(req.text)   # 将cookies转换成列表
        translate = js['translateResult'][0][0]['tgt']
        print(content+'：'+translate)
        return translate


from tkinter import * #窗口模型
class Application(object):
    def __init__(self):
        self.window = Tk()
        self.fanyi = translates()
        self.window.title(u'B哥牌的翻译')   #Unicode是書寫國際文本的標準方法。如果你想要用非英語寫文本,那麼你需要有一個支持Unicode的編輯器。
                                    #類似地,Python允許你處理Unicode文本——你只需要在字符串前加上前綴u或U。
        #设置窗口大小和位置
        self.window.geometry('310x370+500+300')     # （+） 是指出现在屏幕的位置
        self.window.minsize(310,370)
        self.window.maxsize(310,370)
        #创建一个文本框
        self.result_text1 = Text(self.window,bg='azure')
        self.result_text1.place(x = 10,y = 5,width = 285,height = 152)
        self.result_text1.bind("<Key-Return>",self.submit1)    #回车翻译

        #创建一个按钮
        #为按钮添加事件
        self.submit_btn = Button(self.window,text=u'翻译',command = self.submit)
        self.submit_btn.place(x = 205,y = 165,width = 35,height = 25)
        self.submit_btn2 = Button(self.window,text=u'清空',command = self.clean)
        self.submit_btn2.place(x = 250,y = 165,width = 35,height = 25)

        #翻译结果
        self.result_text = Text(self.window,bg='light cyan')
        self.result_text.place(x=10,y=195,width=285,height=165)

        #翻译结果标题
        self.title_label = Label(self.window,text=u'翻译结果')
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
