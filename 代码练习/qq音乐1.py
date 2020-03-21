import requests,openpyxl
# from bs4 import BeautifulSoup
from bs4 import *
lists =[]
def wb():
    web = requests.get('https://y.qq.com/n/yqq/singer/001BLpXF2DyJe2.html#stat=y_new.singerlist.singerpic')
    web.encoding='utf-8'
    singer = BeautifulSoup(web.text,'html.parser')
    name = singer.find_all('a',class_="js_song")
    print(len(name))
    for i in range(len(name)):
        a = name[i]['title']
        b = 'https://y.qq.com/n/yqq/singer/001BLpXF2DyJe2.html'+name[i]['href']
        c = (a,b)
        lists.append(list(c))
    print(lists)

def inputs():
    wb = openpyxl.Workbook()
    a = wb.active
    for i in lists:
        a.append(i)
        wb.save(r'C:\Users\e5bb96\Desktop\name.xlsx')

wb()