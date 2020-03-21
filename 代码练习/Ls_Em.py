import smtplib
#SMtP (Simple Mail Transfer Protocol) '简单邮件传输协议'
from email.mime.text import MIMEText
#引入email包中构建文本内容的方法
from email.header import Header   #引入Header()用来构建邮件头
import csv

class Em:
    def __init__(self):
        self.smtp_server = 'smtp.qq.com'   #(XXstmp邮箱服务器地址)
        self.port = 25  # 465或587 默认25
        self.from_addr = '1324143371@qq.com'    #登录邮箱的用户名  ,#from_addr:邮件发送地址
        self.to_addr = '1255313794@qq.com'      #to_addr :邮件收件人地址
        self.password = 'mqhnnahdjmokhjhb'    #password:授权码

        self.text = '''您好！
            我爱你
            从那一天起
            无法自拔'''
        # ①文本内容，可定义     ②文本类型，默认为plain(纯文本)    ③文本编码，中午为"utf-8"
    def text_(self):    
        msg = MIMEText(self.text,'plain','utf-8')

        msg['From'] = Header('e5bb96')    #发件人名字
        msg['To'] = Header(','.join(self.to_addr))     #收件人名字
        msg['Subject'] = Header('python text')  #主题,题目

        #  开启发信服务，这里使用的是加密传输
        server = smtplib.SMTP()   #如果端口是用SLL加密，则smtplib.SmTP_SLL(端口465)
        server.connect(self.smtp_server,self.port)
        server.login(self.from_addr,self.password)      #login(登录指定的服务器)
        #发送邮件
        server.sendmail(self.from_addr,self.to_addr,msg.as_string())
        #mas.as_string():为一个字符串类型:as_string()是将发送的信息msg变为字符串
        server.quit()

class Eve_Em:
    def __init__(self):    
        self.from_addr = '1324143371@qq.com'
        self.password = 'mqhnnahdjmokhjhb'
        self.smtp_server = 'smtp.qq.com'
        self.text = 'send by python'
        self.date = [['大哥','1255313794@qq.com'],['二哥','1355152664@qq.com']]

    def send(self):
        with open (r'C:\Users\e5bb96\Desktop\to_addrs.csv','w',newline='') as f:
            writer = csv.writer(f)
            for row in self.date:
                writer.writerow(row)

        with open (r'C:\Users\e5bb96\Desktop\to_addrs.csv','r') as f:
            reader = csv.reader(f)
            for row in reader:
                to_addrs = row[1]
                msg = MIMEText(self.text,'plain','utf-8')
                msg['From'] = Header('e5bb96')    
                msg['To'] = Header(to_addrs)    
                msg['Subject'] = Header('python text') 
                server = smtplib.SMTP()
                server.connect(self.smtp_server,25)
                server.login(self.from_addr,self.password)
                try:
                    server.sendmail(from_addr,to_addrs,msg.as_string())
                    print('发送成功')
                except:
                    print('发送失败，请重试')
        server.quit()