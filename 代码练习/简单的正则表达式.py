import re   #引用正则表达式  regular Expression

text = ''
with open (r'C:\Users\e5bb96\Desktop\poem.txt','r') as fp:
    line = fp.readline()
    for i in line:
        text = text + i
fp.close()
print(text+'\n')

result = re.findall('.an..',text)   #查找(其中.代表一个字符包括空格)
print(result)
print('\n')

result = re.findall(' ([ag][a-z][a-z]) ',text) #查找([a-z]表示查找其中一个字符)
                                                 #小括号表示只取括号里面的部分
print(result)
print('\n')
result = re.findall(' *([ag][a-z][a-z]) ',text)           # < a* > 表示能匹配任意多个字符,可以匹配到（空，a，aa...）
print(result)
print('\n')
result = set(result)        #set (去掉查找中重复的语句)
print(result)
print('\n')


print('===========================================================================')
result = re.findall(' (a[a-z][a-z]) | (c[a-z][a-z])',text)
print(result)
final_result = set()
for pair in result:
    if (pair[0] not in final_result):
        final_result.add(pair[0])
    if (pair[1] not in final_result):
        final_result.add(pair[1])
final_result.remove('')  #去除('')
print(final_result)


results = re.findall('\d+',text)  #查找数字      \d+可以匹配到(1个到多个数字，但不包括'空字符')   与 *有别
print(results)                              
      # {}限制数字个数
results = re.findall('\d{0,1}',text)            
results = set(results)
print(results)
