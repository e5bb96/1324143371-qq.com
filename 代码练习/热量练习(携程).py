from gevent import monkey
monkey.patch_all()
import gevent,requests,csv
from bs4 import BeautifulSoup
from gevent.queue import Queue

work = Queue()

url_1 = 'http://www.boohee.com/food/group/{type}?page={page}'
for x in range(1,3):
    for y in range(1,3):
        real_url = url_1.format(type=x,page=y)
        work.put_nowait(real_url)
url_2 = 'http://www.boohee.com/food/view_menu?page={}'
for i in range(1,4):
    real_url = url_2.format(i)
    work.put_nowait(real_url)
lists=[]
alls=[]
def crawler():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    while not work.empty():
        url = work.get_nowait()
        res = requests.get(url,headers=headers)
        soup = BeautifulSoup(res.text,'lxml')
        foods = soup.find_all('li',class_="item clearfix")
        for i in range(len(foods)):
            food_name = foods[i].find('h4').find('a')['title']
            food_url = 'http://www.boohee.com' + foods[i].find('h4').find('a')['href']
            food_calorie = foods[i].find('p').text
            listss=(food_name,food_url,food_calorie)
            lists=list(listss)
            alls.append(lists)

tasks_list = []
for x in range(3):
    task = gevent.spawn(crawler)
    tasks_list.append(task)
gevent.joinall(tasks_list)

csv_file = open(r'C:\Users\e5bb96\Desktop\crawler.csv','w',newline='')
writer = csv.writer(csv_file)
writer = csv.writer(csv_file)
for i in alls:
    writer.writerow(i)