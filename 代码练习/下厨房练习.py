import requests,re
from bs4 import BeautifulSoup
class cool:
    def cool_1(self):
        all = []
        res_foods = requests.get('http://www.xiachufang.com/category/40076/')
        bs_foods = BeautifulSoup(res_foods.text,'html.parser')   
        list_foots = bs_foods.find_all('div',class_="info pure-u")      #查找最小父级标签
        x = 0
        for (i) in (list_foots):
            auto = i.find('a')      #提取第0个父级标签中的<a>标签
#            name = auto.text[17:-13]   #菜名,使用[17:-13]切去多余数据
            name = re.findall('\S+',auto.text)
            Url = 'http://www.xiachufang.com'+auto['href']
            tag_p = list_foots[x].find('p',class_='ing ellipsis')
            x += 1
            ingredinents = tag_p.text[1:-1]   #食材,使用[1:-1]切掉多余数据
            lists=(name,Url,ingredinents)
            menu=list(lists)
            all.append(menu)
        print(all)

    def cool_2(self):        
        opens = requests.get('http://www.xiachufang.com/category/1000003/')
        texts = BeautifulSoup(opens.text,'html.parser')
        names = texts.find_all('p',class_='name')
        lists = texts.find_all('p',class_='ing ellipsis')
        all = []
        for i in range(len(names)):
            list_food = [re.findall('\S+',names[i].text),'http://www.xiachufang.com'+names[i].find('a')['href'],re.findall('\S+',lists[i].text)]
            all.append(list_food)
        print(all)
opens = cool()
opens.cool_1()
opens.cool_2()