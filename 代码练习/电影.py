import requests
from bs4 import BeautifulSoup
class Wb:
    def __init__(self):
        self.movie_open = requests.get('https://movie.douban.com/top250')
        self.movie_text = BeautifulSoup(self.movie_open.text,'html.parser')
        self.menu = []
    def Mv(self):
        moive_name = self.movie_text.find_all('div',class_="pic")
        for i in range(len(moive_name)):
            moive_number = self.movie_text.find_all('span',class_="rating_num")
            moive_talk = self.movie_text.find_all('span',class_="inq")
            moive_names = self.movie_text.find_all('span',class_="title")
            moive_href = self.movie_text.find_all('div',class_='hd')

            number = moive_number[i].text   #评分
            text = moive_name[i].text[1:-4] #序号
            talk = moive_talk[i].text   #推荐语
            names = moive_names[i].text #电影名
            href = moive_href[i].find('a')['href']  #锁链
            
            lists = (text,names,number,talk,href)
            self.menu = list(lists)
            print(self.menu)
opens = Wb()
opens.Mv()
