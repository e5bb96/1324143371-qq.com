print('小精灵：您好，欢迎古灵阁，请问您需要帮助吗？')
question=input('小精灵：【需要or不需要？】；')
if question == '需要':
    print('小精灵：请问您需要什么帮助呢？')
    choice=int(input('小精灵：【1 存取款；2 货币兑换；3 咨询】；'))
    if choice == 2:
        
        print('小精灵：金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
        many=input('小精灵：请问您需要兑换多少金加隆呢？')
        
        print('小精灵：好的，我知道了，您需要兑换'+many+'金加隆')
        print('那么，您需要付给我\n'+str(int(float(many)*51.3))+'人民币')
    
    if choice == 1:
        print('小精灵会推荐你去存取款窗口')
    else:
        print('小精灵会推荐你去咨询窗口。')
else:
    print('小精灵会礼貌地说\'好的，再见。')
print('程序结束')


print('------------------------------------------------------------------------------------')



 


print('------------------------------------------------------------------------------------')


student = ['小明','小红','小黄','小绿','小兰']
student.append('小黑')
print (student)

student[0]='小花'
print (student)

print (student[5:])
del student[2:3]
print (student)

socres = {'小明':95,'小红':90,'小黄':90}
print (len(socres))
print (len(student))
print (socres)

print (socres['小明'])

del socres ['小红']
socres ['小红']= 85
print (socres)
socres['小刚']=92
del socres['小明']
socres['小明']=100
print (socres)

socres['小明']=90
print (socres)

students=[['小明','小红','小黄','小绿'],['小黑','小白','小芳']]
print (students[1][2])

scores = {'第一组':{'小明':95,'小红':90,'小刚':100,'小美':85},'第二组':{'小强':99,'小兰':89,'小伟':93,'小芳':88}}
print (scores)
print (scores['第一组']['小刚'])

q = {'第一组':['小明','小红','小刚','小美'],'第二组':['小强','小兰','小伟','小芳']}
print (q['第一组'][2])

w = [{'小明':95,'小红':90,'小刚':100,'小美':85},{'小强':99,'小兰':89,'小伟':93,'小芳':88}]
print (w[0]['小刚'])

list1 = [{'嫉妒':'envy'},{'恨':'hatred'},{'爱':'love'}]
dict1 = {1:['cake','scone','puff'],2:['London','Bristol','Bath'],3:['love','hatred','envy']}

print (list1[2]['爱'])
print (dict1[3][0])

townee = [
    {'海底王国':['小美人鱼''海之王''小美人鱼的祖母''五位姐姐'],'上层世界':['王子','邻国公主']},
    '丑小鸭','坚定的锡兵','睡美人','青蛙王子',
    [{'主角':'小红帽','配角1':'外婆','配角2':'猎人'},{'反面角色':'狼'}]
    ]


print (townee[5][1]['反面角色'])





print('------------------------------------------------------------------------------------')




for i in '曹尼玛':
    print (i)

for i in range(10):
    print (520)
    
for i in range(10):
    print (i)

for i in range(1,11):

    print ( '书恒走的第'+str(i)+'天')

for i in range (1,21,4):
    print (i*5)

d={'小明':'醋','小红':'油','小白':'盐','小张':'米'}
for i in d:
    print (d)

d={'小明':'醋','小红':'油','小白':'盐','小张':'米'}
for i in d:
    print (i)

d={'小明':'醋','小红':'油','小白':'盐','小张':'米'}
for i in d:
    print (d[i])


  

a = 1
while a != 21:
    print (a*5)
    a = a + 1



print('------------------------------------------------------------------------------------')




for i in range(1,8):
    if i != 4:
        print (i)

a = 1

while a != 8:
    print (a)
    a = a + 1
    if a == 4:
        a = a + 1 

student = ['小明','小红','小刚']
while student[1] != '小刚':
    del student[0]
    student.append('小明')
    print (student)

n = 3
student = ['小明','小红','小刚']
while n!=0:
    student1 = student.pop(0)
    print (student1)
    student.append(student1)
    print (student)
    n = n - 1

student = ['小明','小红','小刚']
for i in range(3):
    student1 = student.pop(0) 
    student.append(student1)  
    print(student)

    
total=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if ((i != j)and(j != k)and (k !=0)):
                print (i,j,k)
                total+=1
print(total)


print('------------------------------------------------------------------------------------')



for k in range(1,10):
    for i in range(1,10):
        print('{} * {} = {} '.format(i,k,i*k),end= (' '))
        if i == k:
            print('\n')
            break
 

for i in range(1,10):
    for b in range(1,i+1):
        print( '%d X %d = %d' % (b,i,i*b) , end ='  ')
    print('')
    print('')


while i <= 9:
    j = 1
    while j <= i:
        print('%d X %d = %d' % (j,i,i*j),end = '  ') 
        j += 1
    print('\n')
    i += 1




print('------------------------------------------------------------------------------------')




import time
time.sleep(2)
print('自古中华锦明，千古江山流淌') 
time.sleep(2)
print ('但却无一人可稳足于此')
time.sleep(2)
print ('如今终于盼得此人')
time.sleep(2)
name = input ('敢问阁下尊姓大名：')
time.sleep(1)
print('原来是' + name + '大侠，' + '有幸相遇')
time.sleep(1)
age = int(input("敢问大侠芳龄："))
if age >= 50:
    time.sleep(1)
    print('看来大侠是看破红尘之人了')
elif age <= 20:
    time.sleep(1)
    print("大侠年轻有为啊")
else:
    time.sleep(1)
    print('大侠正直壮年，乃独家之绝唱，世人之离骚啊！')
time.sleep(1)
print('既然大侠如此雄姿英发，不妨来玩个小游戏')
import random
times = 5
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            if (i!=j)and(j!=k)and(k!=i):
                print(i,j,k   ,end="  ")

secret = random.choice([123,132,213,231,312,321])
choose = int(input('\n[ls：123，你有5次机会]  请从上面六组数据中抽取其中一组：'))
while (times != 0)and (choose != secret):
    time.sleep(1)

    if choose == secret:
        print ('congratulations')
    else:
        times = times - 1
        print('l am sorry,你还有'+str(times)+'次机会')
        choose = int(input('请重新输入：'))

time.sleep(2)
print('上面那些只是小试牛刀而已\n下面来点真功夫')




print('------------------------------------------------------------------------------------')




list_answer = []
number=1
while 2:
    print('第'+str(number)+'对罪犯')
    one = input('第一个罪犯，你是否认罪：')
    two = input("第二个罪犯，你是否认罪：")
    number = number + 1
    list_answer.append([one,two])
    if (one == '认罪')and (two == '认罪'):
        print('各判十年')
        
    
    elif (one=='认罪')and(two=='不认罪'):
        print('则认罪的人判1年，抵赖的人判20年')
        
    else:
        print('若两人都抵赖，则各判3年。')
        break


movie = {'十二生肖':['成龙','廖凡'],'妖猫传':['黄轩','染谷将太'],'无问西东':['章子怡','王力宏','祖峰']}

actor = input ('你最喜欢的演员是：')
for i in movie:
    actors = movie[i]
    
    if actor in actors:

        print(actor+'的电影有'+i)




print('------------------------------------------------------------------------------------')



import time,random
for i in range(1,3):
    time.sleep(1)
    print('------------------------') 
    print('你的第'+str(i)+'次挑战')
    attack = random.randint(30,50)
    red = random.randint(100,150)
    attack1 = random.randint(20,40)
    red1 = random.randint(90,120)
    print('【廖某人】\n血量：'+str(red)+'\n攻击：'+str(attack))  
    print('------------------------') 
    time.sleep(1)
    print('【大水候】\n血量：'+str(red1)+'\n攻击：'+str(attack1))
    print('------------------------')
    time.sleep(1)
    player = red1-attack
    enemy = red-attack1
    while 1:
        time.sleep(1)
        
        print('你发起了攻击，【大水候】剩余血量'+str(player))  
        print('------------------------') 
        if player <= 0:
            time.sleep(1)
            
            print('大水候死左，你赢啦')
            print('------------------------') 
            break
        player = player -attack
        time.sleep(1)
        
        print('大水候向你发起了攻击，【廖某人】剩余血量'+str(enemy))
        print('------------------------') 
        if enemy <= 0:
            time.sleep(1)
            
            print('lose')
            print('------------------------') 
            break 
        enemy =enemy - attack1









import time
import random

player_victory = 0
enemy_victory = 0

while True:
    for i in range(1,4):
        time.sleep(1.5)
        print('  \n——————现在是第 %s 局——————' % i)
        #对比之前：(' \n——————现在是第'+str(i)+'局——————')
        player_life = random.randint(100,150)
        player_attack = random.randint(30,50)
        enemy_life = random.randint(100,150)
        enemy_attack = random.randint(30,50)

        print('【玩家】\n血量：%s\n攻击：%s' % (player_life,player_attack))
        print('------------------------')
        time.sleep(1)
        print('【敌人】\n血量：%s\n攻击：%s' % (enemy_life,enemy_attack))
        print('-----------------------')
        time.sleep(1)

        while player_life > 0 and enemy_life > 0:
            player_life = player_life - enemy_attack 
            enemy_life = enemy_life - player_attack
            print('你发起了攻击，【敌人】剩余血量{}'.format(enemy_life))
            print('敌人向你发起了攻击，【玩家】的血量剩余{}' .format(player_life))
            print('-----------------------')
            time.sleep(1.2)

        if player_life > 0 and enemy_life <= 0:
            player_victory += 1
            print('敌人死翘翘了，你赢了！')
        elif player_life <= 0 and enemy_life > 0:
            enemy_victory += 1
            print('悲催，敌人把你干掉了！')
        else:
            print('哎呀，你和敌人同归于尽了！')

    if player_victory > enemy_victory :
        time.sleep(1)
        print('\n【最终结果：你赢了！】')
    elif enemy_victory > player_victory:
        print('\n【最终结果：你输了！】')
    else: 
        print('\n【最终结果：平局！】')
    recur=input('是否再来一局：')
    if recur == '是':
        continue
    else:
        print('游戏结束!')
        break




A=[91,95,97,99]
B=[92,93,95,98]
number=[]
A.extend(B)
print('合并A,B：{}'.format(A))
A.sort()
print('排序：{}'.format(A))
import numpy as np
average=np.mean(A)
print('平均成绩：{}'.format(average))
median=np.median(A)
print('中位数：{}'.format(median))
for socre in A:
    if socre < average:
        number.append(socre)
print('低于平均成绩的有：{}'.format(number))

#与上面结果相同
scores3 = np.array(A)
print('低于平均成绩的有：{}'.format(scores3[scores3<average]))





import random
apprtizer = ['话梅花生','拍黄瓜','凉拌三丝']
def coupon(money):
    if money < 5:
        a = random.choice(apprtizer)
        return a 
    elif 5 < money < 10:
        b = random.choice(apprtizer)
        return b , '溏心蛋'

print(coupon(3))
print(coupon(6))
print(type(coupon(6)))   #这是一个元组<class 'tuple'>
result = coupon(6)
print(result[1:2])
dish,egg = coupon(7)
print(dish)




rent = 3000
variable_cost=0
def cost():
    global variable_cost
    utilities = int(input('请输入本月的水电费用'))
    food_cost = int(input('请输入本月的食材费用'))
    variable_cost = utilities + food_cost
    print('本月的变动成本是' + str(variable_cost))

def sum_cost():
    sum = rent + variable_cost
    print('本月的总成本是' + str(sum))

cost()
sum_cost()

print('==============================')
def cost1():
    waterfee = int(input('请输入水费：'))
    food_fee = int(input('请输入饭钱：'))
    all_fee = waterfee + food_fee
    print('本月的变动成本{}'.format(all_fee))
    return all_fee

def cost2():
    allfee = rent + cost1()
    print('本月的总成本'+str(allfee))

cost2()




def div (num1,num2):
    growth = (num1 - num2)/num2
    percent = str(growth * 100) + '%'
    return percent

def warning():
    print('Errot:你确定上个月一毛钱都不增不灰？')

def main():
    while True:
        num1 = float(input('请输入本月所获利润：'))
        num2 = float(input('请输入上月所获利润：'))
        if num2 == 0:
            warning()
            continue
        else:
            print("本月的利润增长率：{}".format(div(num1,num2)))
            break

main()



def money():
    name = input('请输入姓名：')
    time = int(input('请输入工作时间为（填【】个月）：'))
    if time < 6:
        yuan = 500
        pass
    elif 6 <= time <= 12:
        yuan = time * 120
        pass
    elif 12 < time:
        yuan = time * 180
        pass
    print('{}奖金：{}'.format(name,yuan))

money()



import random,time

luckylist = ['海绵宝宝','派大星','章鱼哥']
a = random.choice(luckylist)
for i in range(3):
    print('开奖倒计时',3-i)
    time.sleep(1)
images = '''
 /\_)o<
|......\\
| O . O|
\_____/
'''
print(images)
print('恭喜{}中奖'.format(a))






import math

# 变量key代表循环运行程序的开关
key = 1

# 采集信息的函数
def myinput():
    choice = input('请选择计算类型：（1-工时计算，2-人力计算）')
    if choice == '1':
        size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
        number = int(input('请输入人力数量：（请输入整数）'))
        time = None
        return size,number,time
        # 这里返回的数据是一个元组
    if choice == '2':
        size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
        number = None
        time = float(input('请输入工时数量：（请输入小数）'))
        return size,number,time
        # 这里返回的是一个元组

# 完成计算的函数
def estimated(my_input):
    # 把元组中的数据取出来
    size = my_input[0]
    number = my_input[1]
    time = my_input[2]
    # 人力计算
    if (number == None) and (time != None):
        number = math.ceil(size * 80 / time)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number)) 
    # 工时计算
    elif (number != None) and (time == None):
        time = size * 80 / number
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))  

# 询问是否继续的函数
def again():
    # 声明全局变量key，以便修改该变量
    global key
    a = input('是否继续计算？继续请输入y，输入其他键将结束程序。')
    if a != 'y':
        # 如果用户不输入'y'，则把key赋值为0
        key = 0  

# 主函数
def main():
    print('欢迎使用工作量计算小程序！')
    while key == 1:
        my_input = myinput()
        estimated(my_input)
        again()
    print('感谢使用工作量计算小程序！')

main()




import random,time
computer_mode=['剪刀','石头','布']
key,user_choice,computer_choice=1,0,0
def computer():
    global computer_choice
    computer_choice = random.choice(computer_mode)
    print('电脑的出拳为：{}'.format(computer_choice))
    return computer_choice

def user():
    global user_choice
    user_choice = input('请出拳：【输入石头，剪刀或布】')
    while True:
        if user_choice in computer_mode:
            break
        else:
            user_choice = input('输入有误，请重新出拳:')
            continue
    return user_choice

def compare():
    while True:
        if computer_choice == user_choice :
            print('平手,再来一次')
            user()
            time.sleep(1)
            computer()
            time.sleep(1)
            continue
        elif user_choice==computer_mode[computer_mode.index(computer_choice)-1]:    #computer_mode.index()
            print('你输了')
            break
        else:
            print('你赢了')
            break

def again():
    global key
    a = input('是否继续计算？继续请输入y，输入其他键将结束程序。')
    if a != 'y':
        key = 0

def over():
    print('欢迎使用工作量计算小程序！')
    while key == 1:
        user()
        time.sleep(1)
        computer()
        time.sleep(1)
        compare()
        time.sleep(1)
        again()
    print('感谢使用工作量计算小程序！')
over()





print('===========================================================================================')
while True:
    try:
        a = float(input('请输入被除数：'))
        b = float(input('请输入除数：'))
        c = a / b
        print(a,'/',b,'=',c)
        break
    except ZeroDivisionError:
        print('除数不能为0')
    except ValueError:
        print ('请输入数字')


class Computer:
    def __init__ (self):
        self.computer_name = input('请为我起名字：')
        self.name = input('请问，你的名字是：')
        print('你好，{}。我是{}。遇见你真好'.format(self.name,self.computer_name))

    def my_hope(self):
        self.hope = input('你的愿望是:')
        print('{}的愿望是：'.format(self.name))
        for i in range(3):
            print(self.hope)

run = Computer()
run.my_hope()


print('===========================================================================================')

class Chiness:
    def land_area(self,area):
        print('我们居住的地方，陆地面积是%d'% area)
        
class Cantonese(Chiness):
    #间接对方法进行重写
    def land_area(self,area,rate=0.0188):
        Chiness.land_area(self,area * rate)
        #直接继承父类方法，在调整参数。

gonger = Chiness()
yewen = Cantonese()
gonger.land_area(960)
yewen.land_area(960)



print('===========================================================================================')


#法一：
class Chinese:
    name = '廖某人'
    def say(self,someone):
        print(someone + '是中国人')

person = Chinese()
person.say('廖某人')

#法二：
name = 0
class Chinese:
    global name
    name = '廖某人'
    def say(self):
        print(name + '是中国人')

person = Chinese()
person.say()

#法三：
class Chinese:
    name = '廖某人'
    def say(self):
        print(self.name + '是中国人')

person = Chinese()
person.say()

#法四：
class Chinese:
    def __init__(self):
        self.name = '廖某人'
    def say(self):
        print('{}是中国人'.format(self.name))

person = Chinese()
person.say()


print('===========================================================================================')

class Teachar:
    face = '严肃'

class Father:
    face = '甜蜜'

class Student(Teachar,Father):
    pass

class Son(Teachar,Father):
    face = 'gentle'

time3 = Student()
time4 = Son()
print(time3.face)
print(time4.face)




class Student:
    def __init__(self,name,job=None,time=0.00,time_effective=0.00):
        self.name = name
        self.job = job 
        self.time = time 
        self.time_effective = time_effective

    def count_time(self,hour,rate):
        self.time += hour
        self.time_effective += hour * rate

class Programmer(Student):
    def __init__(self, name):
        Student.__init__(self, name ,job='programmer', time=0.00, time_effective=0.00)
    
    def count_time(self, hour, rate=1):
        Student.count_time(self , hour,rate)

student1 = Student('廖某人')
student2 = Programmer('谭某人')
print(student1.job)
print(student2.job)
student1.count_time(10,0.8)
student2.count_time(10)
print(student1.time_effective)
print(student2.time_effective)


class World:   #法一如下
    def __init__ (self):
        self.cheer = '加油'

    def china(self):
        return '中国{}'.format(self.cheer)

people = World()
print(people.china())

class world:   #法二如下
    def __init__(self):
        self.cheers = 'cheer'
    def __str__ (self):
        return 'china {}'.format(self.cheers)
success = world()
print(success)
    

class Book:
    def __init__ (self,name,author,comment,state = 0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state

    def __str__(self):
        states = '未借出'
        if self.state == 1 :
            states = '已借出'
        return '名称：《{}》 作者：{} 推荐语：{} 状态：{}'.format(self.name,self.author,self.comment,states)

class BookManager:
    books = []
    def __init__(self):
        book1 = Book('像自由一样美丽','林达','你要用光明来定义黑暗，用黑暗来定义光明')
        book2 = Book('心是孤独的猎手','卡森·麦卡勒斯','我们渴望倾诉，却从未倾听。女孩、黑人.....',1)
        book3 = Book('活着','余华','荒荡的人生')
        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)

    def menu(self):
        print('欢迎使用流浪图书馆系统，每本沉默的好书都是一座流浪的岛屿。')
        while True:
            print('''1.查询所有书籍\n2.添加书籍\n3.借阅书籍\n4.归还书籍\n5.查询作者的相关书籍\n6.退出系统''')
            choice =  int(input('请输入数学选择对应的功能：'))
            if choice == 1:
                self.show_all_book()
            elif choice == 2:
                self.add_book()
            elif choice == 3:
                self.lend_book()
            elif choice == 4:
                self.return_book()
            elif choice == 5:
                self.author_name()
            elif choice == 6:
                print('感谢使用')
                break
            
    def show_all_book(self):
        for book in self.books:
            print(book)

    def add_book(self):
        new_name = input('请输入书籍名称：')
        new_author = input('请输入作者名称：')
        new_comment = input('请输入书籍推荐语：')
        new_book = Book(new_name,new_author,new_comment)
        self.book.append(new_book)
        print('载入成功')

    def check_book (self,name):
        for book in self.books:  # book相当于实例 book = Book()
            if book.name == name:
                return book #返回该实例对象，遇到return语句方法停止执行
        else:   #代表for else 指 for循环完后执行else
            return None

    def lend_book(self):
        name = input('请输入你需要借阅的书名：') 
        res = self.check_book(name)
        if res != None:
            if res.state == 1 :
                print('你来晚了一步，书已被借阅!')
            else:
                print('借阅成功!')
                res.state = 1 
        else:
            print('该书暂时没有收录在系统里!')

    def return_book(self):
        names = input('请输入你需要归还的书名：')
        res = self.check_book(names)
        if res != None:
            if res.state == 1:
                res.state = 0                
                print('书已归还')
            else:
                print('该书未借出')
        else:
            print('该书暂时没有收录在系统里!')

    def author_name(self):
        authors = input('请输入作者名称：')
        for book in self.books:
            if authors ==  book.author:
                print(book)
            else:
                print('该图书馆没有该作者的相关书籍')
        else:
            return None
manager = BookManager()
manager.menu()


class FictionBook(Book):
    def __init__(self, name, author, comment, state=0, type='虚构类'):
        Book.__init__(self,name,author,comment,state = 0)
        self.type = type

fictionbook = FictionBook('活着','余华','荒荡的人生')
print(fictionbook)


class A (object):
    def __init__ (self):
        self.namea = 'aaa'
    def funca(self):
        print('function :%s' %(self.namea))
#  子类继承父类法①
class B(A):
    def __init__ (self):
        A.__init__(self)
        self.namea = 'bbb'
#  子类继承父类法②
class C(A):
    def __init__(self):
        super(C,self).__init__()
        self.namea = 'ccc'
    def funca(self):
        A.funca(self)
a = A()
a.funca()
b = B()
b.funca()
c = C()
c.funca()


print('廖'.encode('utf-8'))  #'你想编码的内容'.encode('你使用的编码表')             
print('廖'.encode('gbk'))
print(b'\xe5\xbb\x96\xe6\x9f\x90\xe4\xba\xba'.decode('utf-8'))  #'你想解码的内容'.decode('你使用的编码表')
print(b'\xcc\xb7\xd2\xb6\xcd\xa9'.decode('gbk'))          #编码表（ASCII码，GB3212、GBK码，Unicode码，UTF-8码）
#  最前面的字母b，代表bytes（字节）类型的数据
print(type('廖'))
print(type(b'\xe5\xbb\x96'))
print(type(b'\xc1\xce'))   # \n 为分隔号
print(b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0'.decode('utf-8'))
print('K'.encode('ASCII'))  #前者K占两个字节，后者占一个