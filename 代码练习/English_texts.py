import requests,json
from collections import ChainMap
print('程序会在你的D盘下创建两个txt文件,用来存放你的单词积累')
print('')
#print('期间若想退出程序请输入q')
def select():
    global choose
    url = 'https://www.shanbay.com/api/v1/vocabtest/category/'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
    params = {'_': '1572745528283'}
    a = requests.get(url,params=params,headers=headers)
    b = a.json()
    c = b['data']
    for i in range(10):
        print(str(i+1)+' '+c[i][1],end='   ')
    while True:
        try:
            num = int(input("\n请输入需要测试的内容前面的序号："))
            if (1<=num<=10):
                break
            else:
                print('输入有误，请重新输入')
        except:
            print('error')
            pass
    choose = c[num-1][0]
    return choose    

def enter():
    global alls
    ture_number = 0
    alls = []
    unknown={}
    known = {}
    url1 = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/'
    headers1 = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
    params1 = {'category': choose,
        '_': '1572745414114'}
    a = requests.get(url1,headers=headers1,params=params1)
    b = a.json()
    c = b['data']
    while True:
        try:
            number = int(input('请输入测试的单词数量(最大50)：'))
            if (1<=number<=50):
                for i in range(number):
                    word = c[i]['content']
                    ifs = input(str(i+1)+'   是否认识'+' '+word+'  '+'（认识输入y,否则直接按 Enter或任意键）:')
                    print('')
                    if ifs == 'y':
                        m=1
                        for n in c[i]['definition_choices']:
                            if n['pk'] == c[i]['pk']:
                                t_mean = n['definition']
                            print(str(m)+n['definition'])
                            m+=1
                        nums = int(input('\n请输入正确的意思（输入序号）：'))
                        if c[i]['definition_choices'][nums-1]['pk'] == c[i]['pk']:
                            print('Ture！\n')
                            known[word]=t_mean
                            ture_number+=1
                        else:
                            print('error!\n')
                            unknown[word]=t_mean
                            print(word+'：'+t_mean+'\n')
                    else:
                        for n in c[i]['definition_choices']:
                            if n['pk'] == c[i]['pk']:
                                unknown[word]=n['definition']
                                print(word+'：'+n['definition']+'\n')
                break
            else:
                print('输入有误，请重新输入')
        except:
            print('error')
            pass
    alls.append(known)
    alls.append(unknown)
    print('回答正确的单词数量为：'+str(ture_number)+'\n回答错误的单词数量为：'+str(number-ture_number))
    return alls

def safe():
    try:
        with open(r'D:\Knwon_wrod.txt','r') as c:
            dic = eval(c.read())    #读取的str转换为字典
        alls1=alls[0]
        for key in dic.items():     #历遍字典的健
            for key1 in alls[0]:
                if key == key1:
                    alls1 = alls1.pop(key1)        #Python字典的pop()方法（删除字典给定键 key 所对应的值，返回值为被删除的值）
        all_dic = dict(ChainMap(dic,alls1))       #合并两个字典
    except :
        pass
    with open(r'D:\Knwon_wrod.txt','w') as f:
        try:
            f.write(str(all_dic))   #把字典转化为str
        except:
            f.write(str(alls[0]))
    try:
        with open(r'D:\unKnwon_wrod.txt','r') as d:
            dics = eval(d.read())    #读取的str转换为字典
        alls2=alls[1]
        for key in dic.items():     #历遍字典的健
            for key2 in alls[1]:
                if key == key2:
                    alls2 = alls2.pop(key2)        #Python字典的pop()方法（删除字典给定键 key 所对应的值，返回值为被删除的值）
        all_dics = dict(ChainMap(dics,alls2))        #合并两个字典
    except :
        pass
    with open(r'D:\unKnwon_wrod.txt','w') as g:
        try:
            g.write(str(all_dics))   #把字典转化为str
        except:
            g.write(str(alls[1]))

def main():
    choose = select()
    alls = enter()
    safe()
    while True:
        a = int(input('\n1：查看以往全部正确的单词：\n2：查看以往全部错误的单词：\n3：重新测试：\n4:退出                ：'))
        if a == 1:
            with open(r'D:\Knwon_wrod.txt','r') as c:    
                dic_ = eval(c.read())    #读取的str转换为字典
            for key_ in dic_.items():
                print(key_)
        if a == 2:
            with open(r'D:\unKnwon_wrod.txt','r') as g:
                dict_ = eval(g.read())
            for keys in dict_.items():
                print(keys)
        if a == 3:
            choose = select()
            alls = enter()
            safe()
        if a == 4:
            print('\n     谢谢使用!')
            break
        else:
            pass

main()