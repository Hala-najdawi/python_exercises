#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:58:19 2019

@author: owner
"""

from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from tkinter import scrolledtext
import functools
root=Tk()
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
w="500x500+"+str(int((screen_width-500)/2))+"+"+str(int((screen_height-500)/2))
root.geometry(w)
Emplist=[]
Stdlist=[]
class Person:
    def __init__(self,name:str,address:str):
        self._name = name
        self._address = address
    def getname(self,name):
        return self._name
    def setname(self,name):
        self._name=name
    def getadress(self,name):
        self._adress
    def setadress (self,adress ):
          self._adress=adress
    def __del__(self):
        print ( self._name +'I have been deleted person')
class Student(Person):
     def __init__(self,number:int,name,address,subject:str,marks:object):
         super().__init__(name,address)
         self.number = number
         self.__subject=subject
         self.__marks= marks
     def getSubject(self):
      return self.__subject
     def setsubject(self,subject):
          self.__subject=subject
     def getMarks(self):
       return self.__marks
     def setMarks(self,marks):
         self.__marks=marks
     def Average(self):
         result=0
         for mark,markval in self.__marks.items():
              result=markval+result
         return result/len(self.__marks)
     def MarkofA(self):
         x=0
         for mark,markval in self.__marks.items():
             if markval>=90:
                   x=x+1
         return x
     def print_info(self):
               return(f'''
                         Name:{self._name}
                         Address:{self._address}
                         Number:{self.number}
                         subject:{self.__subject}
                         marks:{self.__marks}
                         Average:{self.Average()}
                         ''')
     def __del__(self):
         print ("I have been deleted student")
class Employee(Person):
     def __init__(self,number:int,name,address:str,salary:float,jobtitle:str,loans:list):
          super().__init__(name,address)
          self.number = number
          self.__salary = salary
          self.__jobtitle =jobtitle
          self.__loans = loans
     def getsalary(self):
        return self.__salary
     def setsalary(self,salary):
        self.__salary=salary
     def getjobtitle(self):
        return self.__jobtitle
     def setjobtitle(self,jobtitle):
        self.__jobtitle=jobtitle
     def getloans(self):
        return self.__loans
     def loanstotal(self):
        total=sum(self.__loans)
        return total
     def loansmax(self):
         if(len(self.__loans))==0:
            maxloans="Empty"
         else:
            maxloans=max(self.__loans)
         return maxloans
     def loansmin(self):
         if(len(self.__loans))==0:
            minloans="Empty"
         else:
            minloans=min(self.__loans)
         return minloans
     def setloans(self,loans):
        self.__loans=loans
     def __del__(self):
        print ('I have been deleted employee')
     def infoEmployee(self):
             return(f'''
                         Name:{self._name}
                         Address:{self._address}
                         Number:{self.number}
                         salary:{self.__salary}
                         job title:{self.__jobtitle}
                         total loans:{self.loanstotal()}
                         ''')

def deleteStudent() :
    global Stdlist
    c =Toplevel(root)
    c.title("Delete Student")
    Label(c,text =" Student Number ").grid(row=0, column=0)
    Value=IntVar()
    Number = Entry(c, textvariable=Value).grid(row=0, column=1)
    print (type(Value))
    b = Button(c, text="Delete", command=lambda:f1(Value.get()))
    b.grid(row=1, column=1)
def f1 (Value):
    global Stdlist
    print (type(Value))
    test = list(filter(lambda x: not int(x.number) == Value, Stdlist))
    print(test)
    Stdlist = test[:]

    
    
def deleteEmp() :
    global Emplist
    c =Toplevel(root)
    c.title("Delete Employee")
    Label(c,text =" Employee Number ").grid(row=0, column=0)
    Value=IntVar()
    Number = Entry(c, textvariable=Value).grid(row=0, column=1)
    print (type(Value))
    b = Button(c, text="Delete", command=lambda:f(Value.get()))
    b.grid(row=1, column=1)
def f (Value):
    global Emplist
    print (type(Value))
    test = list(filter(lambda x: not int(x.number) == Value, Emplist))
    print(test)
    Emplist = test[:]    
    
    
def maxloan(Emplist):
    maxlist=[]
    for index,Emp in enumerate( Emplist):
         if type(Emplist[index].loansmax())==int:
            maxlist.append(Emplist[index].loansmax())
    return (max(maxlist))

def listofloan(EmpList):
     totallist=[]
     result=0
     for index,Emp in enumerate( Emplist):
            totallist.append(Emplist[index].getloans())
            totallist.append(Emplist[index].loanstotal())
     for index,employee in enumerate( Emplist):
         result=Emplist[index].loanstotal()+result
     totallist.append(result)
     return (totallist)  
     
def numberofEmployee (Emplist):
    return(len(Emplist))
def minloan(Emplist):
    minlist=[]
    for index,employee in enumerate( Emplist):
         if type(Emplist[index].loansmin())==int:
            minlist.append(Emplist[index].loansmin())
    return (min(minlist))


def hightssalary(Emplist):
     maxsalary=[]
     for index,Emp in enumerate( Emplist):
         maxsalary.append(Emplist[index].getsalary())
     return(max(maxsalary))
     
def lowestsalary(Emplist):
     minsalary=[]
     for index,employee in enumerate( Emplist):
         minsalary.append(Emplist[index].getsalary())
     return(min(minsalary))
   

def numberofStudent(Stdlist):
    return(len(Stdlist))
def maxavg(Stdlist):
    maxlist=[]
    for index,student in enumerate(Stdlist):
        maxlist.append(Stdlist[index].Average())
    return (max(maxlist))
def MarkA(Stdlist):
  for index,student in enumerate(Stdlist):
        if Stdlist[index].MarkofA()>0:
            return (Stdlist[index].print_info())


def alldata():
   c=Toplevel(root)
   txt = scrolledtext.ScrolledText(c, width=200, height=200, wrap=WORD)
   txt.insert(END, "number of Employee: "+str(numberofEmployee(Emplist)))
   txt.insert(END, "\n")
   txt.insert(END, "Max loan : "+str(maxloan(Emplist)))
   txt.insert(END, "\n")
   txt.insert(END, "list of loan  "+str(listofloan(Emplist)))
   txt.insert(END, "\n")
   txt.insert(END, "min loan "+str(minloan(Emplist)))
   txt.insert(END, "\n")
   txt.insert(END, "minsalar "+str(lowestsalary(Emplist)))
   txt.insert(END, "\n")
   txt.insert(END, "maxsalary "+str(hightssalary(Emplist)))
   txt.insert(END, "\n")
   txt.insert(END, "__________________________________________")
   txt.insert(END, "\n")
   txt.insert(END, "number of student "+str(numberofStudent(Stdlist)))
   txt.insert(END, "\n")
   txt.insert(END, "number of student "+str(maxavg(Stdlist)))
   txt.insert(END, "\n")
   txt.insert(END, "number of student "+str(MarkA(Stdlist)))
   
   txt.yview(END)
   txt.pack()

def addemployee():
     
    EmpWin=Toplevel(root)
    EmpWin.title('Employee window')
    EmpWin.geometry('400x250')
    name=Label(EmpWin,text="Number").place(x=30,y=50)
    email=Label(EmpWin,text="Name").place(x=30,y=90)
    address=Label(EmpWin,text="adress").place(x=30,y=120)
    salary=Label(EmpWin,text="salary").place(x=30,y=150)
    jobtitle=Label(EmpWin,text="jobtitle").place(x=30,y=170)
    loans=Label(EmpWin,text="loans").place(x=30,y=200)
    val1=IntVar()
    val2=StringVar()
    val3=StringVar()
    val4=StringVar()
    val5=StringVar()
    val6=StringVar()  
    e1=Entry(EmpWin,textvariable=val1).place(x=100,y=50)
    e2=Entry(EmpWin,textvariable=val2).place(x=100,y=90)
    e3=Entry(EmpWin,textvariable=val3).place(x=100,y=120)
    e4=Entry(EmpWin,textvariable=val4).place(x=100,y=150)
    e5=Entry(EmpWin,textvariable=val5).place(x=100,y=170)
    e6=Entry(EmpWin,textvariable=val6).place(x=100,y=200)
    def SaveEmp():
        loans=[int (i) for i in val6.get().split(",")]
        NewEmp=Employee(val1.get(),val2.get(),val3.get(),val4.get(),val5.get(),loans)
        print(NewEmp.infoEmployee())
        Emplist.append(NewEmp)
    button=Button(EmpWin,text="Save",command=SaveEmp).place(x=150,y=220)

def viewEmp():
    c=Toplevel(root)
    txt = scrolledtext.ScrolledText(c, width=200, height=200, wrap=WORD)
    for emp in Emplist:
        txt.insert(END, "infoEmployee: "+str(emp.infoEmployee())+ "\n")
        txt.insert(END, "________________ \n")
    txt.yview(END)
    txt.pack()
    
def addstudent():
    StdWin=Toplevel(root)
    StdWin.title('Student  window')
    StdWin.geometry('400x250')
    number=Label(StdWin,text="Number").place(x=30,y=50)
    name=Label(StdWin,text="Name").place(x=30,y=90)
    address=Label(StdWin,text="adress").place(x=30,y=120)
    subject=Label(StdWin,text="subject").place(x=30,y=150)
    marks1=Label(StdWin,text="Arabic").place(x=30,y=170)
    marks2=Label(StdWin,text="Math").place(x=30,y=200)
    val1=IntVar()
    val2=StringVar()
    val3=StringVar()
    val4=StringVar()
    val5=IntVar()
    val6=IntVar() 
    e1=Entry(StdWin,textvariable=val1).place(x=100,y=50)
    e2=Entry(StdWin,textvariable=val2).place(x=100,y=90)
    e3=Entry(StdWin,textvariable=val3).place(x=100,y=120)
    e4=Entry(StdWin,textvariable=val4).place(x=100,y=150)
    e5=Entry(StdWin,textvariable=val5).place(x=100,y=170)
    e6=Entry(StdWin,textvariable=val6).place(x=100,y=200)
    def SaveStd():
        mark={"Arabic":val5.get(),"Math":val6.get()}
        Newstd=Student(val1.get(),val2.get(),val3.get(),val4.get(),mark)
        print(Newstd.print_info())
        Stdlist.append(Newstd)
    button=Button(StdWin,text="Save",command=SaveStd).place(x=150,y=220)
def viewstd():
    c=Toplevel(root)
    txt = scrolledtext.ScrolledText(c, width=200, height=200, wrap=WORD)
    for emp in Stdlist:
        txt.insert(END, "infoStudent: "+str(emp.print_info())+ "\n")
        txt.insert(END, "________________ \n")
    txt.yview(END)
    txt.pack()
def Help_1():
    messagebox.showinfo("About us","oop project2")
      
top=Menu(root)
root.config(menu=top)
file=Menu(top,tearoff=0)
file.add_command(label='Report',command=alldata)
file.add_separator()
file.add_command(label='Quit',command=root.destroy)
top.add_cascade(label='File',menu=file)
Employee1=Menu(top,tearoff=0)
Employee1.add_command(label='Add',command=addemployee)
Employee1.add_command(label='View',command=viewEmp)
Employee1.add_command(label='Delete',command=deleteEmp)
top.add_cascade(label='Employee',menu=Employee1)
Students1=Menu(top,tearoff=0)
Students1.add_command(label='Add',command=addstudent)
Students1.add_command(label='View',command=viewstd)
Students1.add_command(label='Delete',command=deleteStudent)
top.add_cascade(label='Students',menu=Students1)
Help=Menu(top,tearoff=0)
Help.add_command(label='About',command=Help_1)
top.add_cascade(label='Help',menu=Help)


root.mainloop()