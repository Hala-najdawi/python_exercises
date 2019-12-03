#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:25:57 2019

@author: owner
"""
"""
def act ():
    if value1.get() == "Orange" and value2.get() == "CodingAcademy" :
         z = messagebox.showinfo("Login", "Successful login")
         print (z)
         if z == "ok":
             parent.destroy()
    else:
         messagebox.showinfo("Login", "Wrong User Name or Password")
parent = Tk()
value1 = StringVar()
value2 = StringVar()
name = Label(parent, text = "Name").grid(row=0, column = 0)
e1 = Entry(parent, textvariable= value1).grid(row = 0, column =1)
password = Label(parent, text ="Password").grid(row = 1, column = 0)
e2 = Entry(parent, textvariable= value2).grid(row = 1, column =1)
submit = Button(parent, text="Submit", command= act).grid(row = 4, column = 0)
parent.mainloop()


"""
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.colorchooser import *
#EX1
"""
parent=Tk()
def check():
    if value1.get() =='orange' and value2.get() =="CodingAcademy":
       print(messagebox.showinfo('login','successful login'))
    else:
         messagebox.showinfo('login','Wrong user name or password')
value1 = StringVar()
value2 = StringVar()
name=Label(parent,text="Name").grid(row=0,column=0)
e1=Entry(parent,textvariable=value1).grid(row=0,column=1)
password=Label(parent,text="Password").grid(row=1,column=0)
e2=Entry(parent,textvariable=value2).grid(row=1,column=1)
submit=Button(parent,text="submit", command=check).grid(row=4,column=0)
parent.mainloop()
"""
#EX2:

def open_child1():
    dialog_title=""
    dialog_text="This is a message"
    answer=messagebox.showinfo(dialog_title,dialog_text)
def open_child2():
    top=Tk()
    top.title('Child window 2')
    top.geometry('400x250')
    name=Label(top,text="Emy Number").place(x=30,y=50)
    email=Label(top,text="Emy Name").place(x=30,y=90)
    e1=Entry(top).place(x=100,y=50)
    e2=Entry(top).place(x=100,y=90)
    button=Button(top,text="Quit",command=top.destroy).place(x=150,y=150)
    button.pack()
    top.mainloop()
def open_child3():
    win=Tk()
    win.title("Welcome")
    win.geometry('350x200')
    txt=scrolledtext.ScrolledText(win,width=40,height=10)
    txt.grid(column=0,row=0)
    for r in range(20):
        print(' ')
    win.mainloop()
root=Tk()
root.title("root window")
Button(root, text="open child window 1", command=open_child1).grid()
Button(root, text="open child window 2", command=open_child2).grid()
Button(root, text = 'open child window 3', command = open_child3).grid()
root.mainloop()

#EX3:
"""
root=Tk()
def getcolor():
    color=askcolor()
    root=config(background=color[1])
Button(text="select color",command=getcolor).pack()
mainloop()
"""
