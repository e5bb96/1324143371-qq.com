from selenium import webdriver
from selenium.webdriver.chrome.options import Options   #从options模板中调用OPtions类
import time
from bs4 import BeautifulSoup

chrome_options = Options()  # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
dirver = webdriver.Chrome(options = chrome_options)    #设置引擎为Chrome,在后台默默运行

# dirver = webdriver.Chrome()     #设置引擎为Chrome，真实的打开一个Chrome浏览器
dirver.get("https://localprod.pandateacher.com/python-manuscript/hello-spiderman/")
time.sleep(2)

pageSource = dirver.page_source     #获取完整渲染的网页源代码  输出'str'类型，实例化
print(type(pageSource))

# label = dirver.find_elements_by_tag_name('label')   #解析网页并提取标签'label'  输出'list'类型
a = dirver.find_element_by_css_selector("[class='xl-chrome-ext-bar']") # selenium中查找某标签有空格用css
labels = dirver.find_element_by_tag_name('label')
print(type(labels))             #解析网页并提取标签'label'  输出'WebElement'类型 
print(labels.text)              #提取文字
print(labels.get_attribute('type'))     #输入参数：属性名，可以提取属性值
# print(type(label))
# for i in label:
#     print(i.text)
# print(label.get_attribute('type'))        #获取属性的值


#find_element_by_link_text  通过链接文本获得超链接
#find_element_by_partial_link_text   通过链接部分文本获得超链接

teacher = dirver.find_element_by_id('teacher')
teacher.send_keys('必须是吴枫呀')   #模拟输入文字
teacher.clear()
teacher.send_keys('吴枫')
assistant = dirver.find_element_by_name('assistant')
assistant.send_keys('都喜欢')
button = dirver.find_element_by_class_name('sub')
button.click()      #模拟点击按钮

time.sleep(1)
dirver.close()





'''
1. id定位：find_element_by_id("id值")；id屬性是唯一的

1 driver.find_element_by_id( " loginName " ).clear() #用戶名輸入框的id屬性
 2 driver.find_element_by_id( " loginName " ).send_keys("admin")
 3 driver.find_element_by_id( " pwdTip " ).send_keys(Keys .TAB) #密碼輸入框的id屬性
 4 driver.find_element_by_id( " pwdTip " ).send_keys("111111")
2. name定位：元素的名稱，find_element_by_name("name值")；name屬性值在當前頁面可以不唯一

1 driver.find_elements_by_name( " PeriodName " )[1].click() # 選擇學段：初中
2 driver.find_elements_by_name( " SubjectName " )[0].click() # 選擇學科：語文
  find_elements_by_name("PeriodName")是因為當前頁面有一組radiobutton的name值是PeriodName，所以可以用定位一組元素的方法findElements，定位出來的是結果一個list

3. class定位：元素的類名，find_element_by_class_name("class值")

driver.find_elements_by_class_name( " u-btn-levred " )[0].click() # 選擇年級：七年級
4. tag定位：頁面html文檔下的各種標籤，find_element_by_tag_name("input")；

tag往往用來定義一類功能，所以通過tag識別某個元素的概率很低。任意打開一個頁面，都會發現大量的<div>、<input>、<a>等tag，所以tag name定位很少用

5. link定位：專門用來定位文本鏈接，find_element_by_link_name("text")；

driver.find_element_by_link_text(u " 退出" ).click() #頁面右上方的一些個人操作，比如退出、個人中心、消息通知等
6. partial link定位：是對link定位的一種補充，當鏈接上的文本內容比較長的時候，可以取文本的一部分進行定位，當然這部分可以唯一地標識這個鏈接

※注：以上的方式稍有局限，且經常頁面沒有id，name這些屬性值，class name重複性較高，link定位有針對性，所以Xpath與Css定位更靈活些。

7. XPath定位：find_element_by_xpath("")；有多種定位策略，用FirePath插件自動生成的涵蓋以下幾種方式

  1）絕對路徑定位：對於沒有id，name、classname不好定位的，這也是我最常用的，因為可以通過Firefox的FirePath插件可以方便的獲取到xpath值

  2）利用元素屬性定位：

　　find_element_by_xpath(".//*[@id='Title']")，這裡是用的id，也可以用元素其他能夠唯一標識的屬性，不局限於id、name、class這些；*代表的是標籤名，不指定時就可以用*代替
'''







'''8. CSS定位（薄弱，用的很少，但很強大，比xpath簡潔靈活）：使用選擇器來為頁面元素綁定屬性，可以靈活地選擇控件的任意屬性；find_element_by_css_selector("")；同樣也可以用FirePATH生成css喲！

  1）通過class屬性定位：點號（"."）表示通過class屬性定位

1 <input class = " u-btn mart5 " type= " submit " onclick= " return User.check() " value= " 登錄" >
 2 driver.find_element_by_css_selector( " .u-btn.mart5 " ).click()
  2）通過id屬性定位：（"#"）表示通過id定位元素

driver.find_element_by_css_selector( " #loginName " )
  3）通過其他屬性定位：（"[]"），中括號裡的屬性可以唯一標識這個元素就可以；屬性的值可以加引號，也可以不加

1 <input class = " u-btn mart5 " type= " submit " onclick= " return User.check() " value= " 登錄" >
 2 driver.find_element_by_css_selector( " [type=submit] " ).click()
  4）組合定位'''