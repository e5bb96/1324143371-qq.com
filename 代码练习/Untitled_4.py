import json,requests
session = requests.session()
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
url = r'https://b2cpush.zhihuishu.com/b2cpush/courseDetail/save2CCoursProgressV2'

t = time.time()
T = str(round(t*1000))
data = {'courseId': '2068219',
'videoId': '460633',
'lessonId': '368843 ',
'learnTime': '6547',
'chapterName': '国际关系研究和学习方法（下）',
'sourceType': '3',
'totalTime': '6546',
'studyMode': '1',
'uuid': 'Xo5j9nL8',
'dateFormate': T}
session.post(url,headers=headers,data=data)
