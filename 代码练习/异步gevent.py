
#  解析说明  https://imgchr.com/i/8WDKED

from gevent import monkey
monkey.patch_all()      #把程序变成协作式运行，实现异步
import time,requests,gevent
from gevent.queue import Queue

start = time.time()

url_list=['https://www.baidu.com/',
'https://www.sina.com.cn/',
'https://www.qq.com/',
'https://www.163.com/',
'https://www.ifeng.com/',
'https://www.tmall.com/']

work = Queue()      #创建列表对象
for url in url_list:
    work.put_nowait(url)
print(work.qsize())   #列表剩余长度

def crawler():
    while not work.empty():     #当队列不是空的时候，就执行任务
        url = work.get_nowait()
        #此处请求需要等待，异步执行
        r = requests.get(url)
        # qsize() 剩余任务
        print(url,work.qsize(),r.status_code)   #返回queue的近似值。注意：qsize>0 不保證(get)取元素不阻塞。qsize< maxsize不保證(put)存元素不會阻塞


tasks_list = []
for x in range(2):      #建两个爬虫
    #确定任务，在未异步执行时crawler函数不执行
    task = gevent.spawn(crawler)
    tasks_list.append(task)
    print(tasks_list)
#两个任务异步执行，当其中一个在等待时，下一个任务启动（此时crawler函数才真正执行）
gevent.joinall(tasks_list)

end = time.time()
print(end-start)