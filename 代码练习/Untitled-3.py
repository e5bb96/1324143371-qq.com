from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time,json,requests
# 鼠标操作
from selenium.webdriver.common.action_chains import ActionChains

chrome_driver = r'C:\Users\e5bb96\AppData\Local\Google\Chrome\Application\chromedriver.exe'
options = Options()
#options.add_argument('--headless')

options.add_experimental_option('excludeSwitches',['enable-logging'])   #解决DevTools監聽ws://127.0.0.1
url1 = "https://onlineh5.zhihuishu.com/onlineWeb.html#/studentIndex"
dirver = webdriver.Chrome(options = options,executable_path=chrome_driver)

# location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
# dirver = webdriver.Firefox(firefox_binary=location)

dirver.get(url1)
time.sleep(2)

# pageSoursce = dirver.page_source # 转换成str型
# soup = BeautifulSoup(pageSoursce,'lxml')
# url2 = soup.find('ul',class_="header-loginStatus fr").find('a')['href']
# print(url2)
# time.sleep(0.5)
# dirver.get(url2)

username = dirver.find_element_by_id('lUsername')
userpassword = dirver.find_element_by_id('lPassword')
In = dirver.find_element_by_css_selector("[class='wall-sub-btn']")
username.send_keys('18675679463')
userpassword.send_keys('xin088748')
In.click()

time.sleep(3)

while(True):
    time.sleep(1)
    slide = dirver.find_element_by_id('nc_1_n1z')       #找到滑块
    ActionChains(dirver).click_and_hold(slide).perform()    #鼠标按住
    ActionChains(dirver).move_by_offset(160,0).perform()    #滑动
    time.sleep(1)
    ActionChains(dirver).move_by_offset(260,0).perform()    #滑动
    F5 = dirver.find_element_by_xpath("//*[@id='nocaptcha']/div/span/a")
    F5.click()

# dirver.close() 
# session = requests.session()
# headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
