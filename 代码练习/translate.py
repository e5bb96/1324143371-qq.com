from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

text = input("请输入你需要翻译的内容：")
#实例化Options对象
chrome_options = Options()
#开启静默模式
chrome_options.add_argument('--headless')
dirver = webdriver.Chrome(options=chrome_options)
dirver.get(r'http://fy.iciba.com/')
time.sleep(2)


inputs = dirver.find_element_by_css_selector("[class='textarea-wrap']").find_element_by_css_selector("[class='textarea']")
inputs.send_keys(text)
click = dirver.find_element_by_css_selector("[class='trans-btn']")
click.click()
translate = dirver.find_element_by_css_selector("[class='res-con']")
try:
    chinese = translate.find_element_by_css_selector(".prop")
    print(chinese.text)
except:
    english = translate.find_element_by_css_selector(".sentence-other")
    print(english.text)

time.sleep(2)
dirver.close()