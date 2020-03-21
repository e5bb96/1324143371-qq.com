import pyautogui,time,sys


#获取鼠标位置
x,y=pyautogui.position()
print('x={},y={}'.format(x,y))
i=0

try:
    while (1):
        #移动鼠标,duration类似于移动时间或移动速度，省略后则是瞬间移动到指定的位置
        pyautogui.moveTo(x=1159,y=603,duration=0.25)
        pyautogui.click(x=1159,y=603,clicks=2,interval=0.0,button='left')
        time.sleep(0.4)
        i+=1

except KeyboardInterrupt:
    sys.exit(0)


# utogui.click()，這個函數的用法如下：

# pyautogui.click(x,y, clicks=1, internal=0.0, button='left')

# 主要使用的參數就是這幾個：

# x表示x坐標：

# y表示y坐標：

# clicks表示點擊的次數，默認值是1internal表示兩次點擊的時間間隔，默認值是0

# button表示用哪個按鍵點擊，默認是left，還可以是right、middle等。