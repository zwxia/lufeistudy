import tkinter as tk
import os
window = tk.Tk()
window.title("工具")
window.geometry('800x400')

l=tk.Label(window,text='this is TK',bg='red',width=15,height=2)#标签控件；可以显示文本和位图
l.pack()#放置
def screencap():
    os.system("截图.bat ")
b1=tk.Button(window,text='截图',width=15,height=2,command=screencap)
b1.pack()
def dcy11_log():
    os.system("导dcy11_log.bat")
b2=tk.Button(window,text='DCY11_log',width=15,height=2,command=dcy11_log)
b2.pack()
def sx11_log():
    os.system("1.5c 导log.bat")
b3=tk.Button(window,text='1.5c_log',width=15,height=2,command=sx11_log)
b3.pack()
def logcat():
    os.system("LOG截取.bat")
b4=tk.Button(window,text='logcat',width=15,height=2,command=logcat)
b4.pack()


window.mainloop()