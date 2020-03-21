name = 'name'
print(len('a'))
a = name[-2:]#print(a)   e          # --->（+)左舍右取
d = name[1:3]#print(d)   am         # <--- (-)左取右舍
b = name[-1:]#print(b)   me     
c = name[:-2]#print(c)   na


#lambda
def sum(x,y):
    return x+y
print(sum(1,2))#相当于
sums = lambda x,y:x+y
print(sums(1,3))

# list(tup) tup--要转换为列表的元组
lists = (123,'xyz','zara','abc')
alist = list(lists)
print(alist)


#filter--判断函数
def is_odd(n):
    return n % 2 == 1
newlist = filter(is_odd,range(10))  #print(newlist)  会出现<filter object at 0x000001B68F052828>
                                        #用 list(newlist)  解决
print(list(newlist))

#reverse ()   翻译 [相反]
lists = [123,'xyz','zara','abc']
lists.reverse()
print(lists)  #['abc', 'zara', 'xyz', 123]

a = [[1,4,3],[3,2,5],[5,1,2,],[4,3,1]]
b=sorted(a,key=lambda _:_[1])
print(b)   #[[5, 1, 2], [3, 2, 5], [4, 3, 1], [1, 4, 3]]
c=sorted(a,key=lambda _:_[0])
print(c)    #[[1, 4, 3], [3, 2, 5], [4, 3, 1], [5, 1, 2]]


a = ['handsome','bruce','boy']
d= sorted(a,key=lambda x:len(x),reverse=True)
print(d)   #['handsome', 'bruce', 'boy']
e = sorted(a,key=lambda x:len(x))
print(e)   #['boy', 'bruce', 'handsome']



#-------------------------------------------------------------------------------------
# 下面注释掉的代码，皆为检验代码（验证每一步的思路和代码是否达到目标，可解除注释后运行）。
file1 = open('winner.txt','w',encoding='utf-8') 
file2 = file1.write('罗恩102\n, 哈利383\n, 赫敏570\n, 马尔福275\n')
file1 = open('winner.txt','r',encoding='utf-8') 
file_lines = file1.readlines() 
file1.close()

dict_scores = {}
list_scores = []
final_scores = []

print(file_lines) 
print(len('\n'))

# 打印结果为：['罗恩102\n', '哈利383\n', '赫敏570\n', '马尔福275\n']
# 经过测试，发现'\n'的长度是1。所以，名字是“第0位-倒数第5位”，分数是“倒数第4位-倒数第二位”。
# 再根据“左取右不取”，可知：name-[:-4],score-[-4:-1]

for i in file_lines:  # i是字符串。
    print(i)
    name = i[:-4]  # 取出名字（注：字符串和列表一样，是通过偏移量来获取内部数据。）
    score = int(i[-4:-1])  # 取出成绩
    print(name)
    print(score)
    dict_scores[score] = name  # 将名字和成绩对应存为字典的键值对(注意：这里的成绩是键)
    list_scores.append(score)

# print(list_scores)
list_scores.sort(reverse=True)  # reverse，逆行，所以这时列表降序排列，分数从高到低。
# print(list_scores)

for i in list_scores:
    result = dict_scores[i] + str(i) + '\n'
    # print(result)
    final_scores.append(result)

print(final_scores)  # 最终结果

winner_new = open('winner_new.txt','w',encoding='utf-8') 
winner_new.writelines(final_scores)
winner_new.close()