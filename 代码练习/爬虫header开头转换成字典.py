strs = '''Host: open.tool.hexun.com
Pragma: no-cache
Cache-Control: no-cache
Accept: */*
Referer: http://stock.hexun.com/gsxw/'''
alls=[]
a = strs.split('\n')  #split('\n')  将空行去掉换成逗号
print(a)
for i in a:
    b = i.split(':',1)   #split(':')   将：去掉换成逗号
    print(b)
    alls.append(b)
print(alls)
c = dict(alls)    #dict(alls)将列表变成字典，逗号变成冒号(:)  （*alls为列表）
print(c)


headers = dict([line.split(":",1) for line in strs.split("\n")])
print(headers)