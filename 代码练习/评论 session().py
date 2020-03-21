import requests,json
session = requests.session()    #session 会议，一段

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
# 避免反爬虫

def read_cookies():
    with open(r'C:\Users\e5bb96\Desktop\context.txt','r',newline='') as cookies_txt:
        cookies_dict = json.loads(cookies_txt.read())  #调用json模板的loads函数，将字符串转换成字典
        cookies = requests.utils.cookiejar_from_dict(cookies_dict)  #从字典转换成cookies格式
        return (cookies)


def write_cookies():
    url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
    data = '''log: spiderman
    pwd: crawler334566
    rememberme: forever
    wp-submit: 登录
    redirect_to: https://wordpress-edu-3autumn.localprod.oc.forchange.cn
    testcookie: 1'''
    data = dict([line.split(":",1) for line in data.split("\n")])   #将headers换成字典
    login_in = session.post(url,headers=headers,data=data) 
    print(login_in)     #输出<Response [200]>说明服务器接收请求
    # print(type(login_in))
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    #将cookies_dict转化成字典
    # print(cookies_dict)
    # print(type(cookies_dict))
    cookies_str = json.dumps(cookies_dict)   #调用json模板的dumps函数，将cookies从字典在转成字符串
    # print(cookies_str)
    # print(type(cookies_str))
    with open(r'C:\Users\e5bb96\Desktop\context.txt','w',encoding='gbk',newline="") as f:
        f.write(cookies_str)

#cookies = login_in.cookies   #调用requests对象的cookies属性获得登录的cookies

def comment_():
    a = input("请输入你要评论的内容：")
    url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
    data_1 = '''comment: ''' + a + '\n' + '''submit: 发表评论
    comment_post_ID: 13
    comment_parent: 0'''
    data_1 = dict([line.split(":",1) for line in data_1.split("\n")])
    comment = session.post(url_1,headers=headers,data=data_1,)#cookies=cookies
    return (comment)
 

try:
    session.cookies = read_cookies()
except FileNotFoundError:   #(找不到文件)
    write_cookies()
    session.cookies = read_cookies()

while True:
    num = comment_()
    if num.status_code==200:          #打印出comment的状态码，若状态码等于200，则证明我们评论成功
        print("成了")
        break
    else:
        print('error,pleas repect')
        write_cookies()
        session.cookies = read_cookies()