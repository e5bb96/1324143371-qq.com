from tkinter import *
import tkinter.messagebox

window = Tk()           #主窗口
window.title('my window')       #窗口标题
# window.resizable(0,0)            #限制窗口调节
window.geometry('500x400')      #窗口尺寸   geometry(几何学)
# #限制窗口尺寸
# window.minsize(400,400)
# window.maxsize(800,800)

def pointer():
    tkinter.messagebox.showinfo('提示','没有内容')

#label(标签)
Label=Label(window,text='hello my boby',background='green')

Label.pack()        #固定窗口位置
#Button(按钮)
button1 = Button(window,text='button1',command=pointer)
button1.pack(side=LEFT)
button2 = Button(window,text='button2')
button2.pack(side=RIGHT)

li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(window)          #  创建两个列表组件
listb2 = Listbox(window)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)
 
for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)
 
listb.pack()                    # 将小部件放置到主窗口中

listb2.pack()


window.mainloop()               #循环消息，让窗口活起来


#====================================================================================

from tkinter import *

window = Tk()
window.title("mt window")
window.geometry('400x300')
# 变量
var = StringVar()
l = Label(window,textvariable=var,bg='green',font=('Arial',12),
width=10,height=2)
e = Entry(window,show='#')      #show 输入内容不可见为'*'
t = Text(window,height=2)

def hit_me():
    var.set('fuck you')
def insert_point():
    var = e.get()
    t.insert('insert',var)
def insert_end():
    var = e.get()
    t.insert('end',var)         #t.insert(1.1,var)   代表往第一行第一列输入数据

b = Button(window,text='hit me',
    width=8,height=2,command=hit_me)
b1 = Button(window,text='insert point',command=insert_point)
b2 = Button(window,text='insert end',command=insert_end)
t.pack()
b1.pack()
b2.pack()
e.pack()
b.pack()
l.pack()

window.mainloop()