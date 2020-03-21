import requests,schedule,time
from bs4 import BeautifulSoup

# spider(蜘蛛)
def weather_spider():
    headers = '''user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'''
    url = 'https://weather.com/zh-CN/weather/today/l/a34f7b6e9a6c22c032474818c958e44723779a9080bbedb7aca653e9717b1ea0'
    headers = dict([i.split(':',1) for i in headers.split('\n')]) #header → dict
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'lxml')
    #container(容器)
    container = soup.find(class_='today_nowcard-section today_nowcard-condition')
    now_temperature = container.find(classname="deg-feels")
    today_nowcards = container.find(class_="today_nowcard-phrase")
    hilo = container.find(class_="deg-hilo-nowcard").find('span')
    hilo_low = container.find(class_="deg-hilo-nowcard").find('span')
    print('当前温度：'+now_temperature.text+'\t'+today_nowcards.text+'\nThe largest temperature is '+hilo.text+'\nThe lowest temperature is '+hilo_low.text)

schedule.every().day.at('12:00').do(weather_spider)
# schedule.every(5).minutes.do(job)
# # 每隔一小时执行一次任务
# schedule.every().hour.do(job)
# # 每天的10:30执行一次任务
# schedule.every().day.at("10:30").do(job)
# # 每5-10分钟执行一次任务
# schedule.every(5).to(10).minutes.do(job)
# # 每周一的这个时候执行一次任务
# schedule.every().monday.do(job)
# # 每周三的13:30执行一次任务
# schedule.every().wednesday.at("13:30").do(job)
# # 每分钟的这个时刻执行一次任务
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

