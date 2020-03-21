import requests,json,time

session = requests.session()

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
url = r'https://translate.googleapis.com/translate_a/t?'
params = '''anno: 3
client: te_lib
format: html
v: 1.0
key: AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw
logld: vTE_20200210_00
sl: zh-CN
tl: zh-TW
sp: nmt
tc: 1
sr: 1
tk: 245543.329905
mode: 1s'''

params = dict([line.split(":",1) for line in params.split("\n")])

data = '''q: <a i=0>公告：</a><a i=1>批阅引擎定期更新  2019-11-06</a><a i=2>更多</a>
q: <a i=0>廖振兴</a><a i=1>设置</a><a i=2>消息 </a><a i=3>退出</a><a i=4>帮助</a>
q: 我的作文
q: 写作文
q: 编号
q: 作文标题
q: 教师
q: 截止日期
q: 成绩
q: 次数
q: 17401
q: The Importance of writing ability and how to develop it
q: 王美绒
q: 2020-03-23
q: 75.5
q: <a i=0>5</a><a i=1>/5</a>
q: <a i=0>修改</a><a i=1>查看</a>
q: 首页
q: 上一页
q: 1
q: 下一页
q: 尾页
q: 跳转到
q: 页
q: 确定
q: <a i=0>新闻公告</a><a i=1>关于全景</a><a i=2>联系我们</a><a i=3>用户反馈</a>
q: <a i=0>© 2018 版权所有 上海外教社信息技术有限公司  </a><a i=1>沪ICP备05013223号-11</a>
q: 已提交次数/最高提交次数
q: 全景智能批阅
q: 下载视频'''

data = dict([line.split(":",1) for line in data.split("\n")])

session.post(url,headers=headers,params=params,data=data)
