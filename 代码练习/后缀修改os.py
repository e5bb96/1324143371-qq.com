import os 
def change():
    # 列出当前目录下所有的文件
    desktops = os.listdir(r'C:\Users\e5bb96\Desktop')
    os.chdir(r'C:\Users\e5bb96\Desktop')
    for i in desktops:
        #os.path.splitexe() (分离文件名和后缀)
        portion = os.path.splitext(i)
        if portion[1]=='.txt':
            new = portion[0]+".bat"
    #  os.rename('oldname','newname')重命名文件/目录
            os.rename(i,new)

