#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 09:50:14 2019

@author: owner
"""
import functools 
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
        
        
    
#Q1
EmployeeList=[]

Employee1=Employee(1000,"Ahmad yazan ","Amamn ,Joradan",500,"HR consultant",[434,200,1020])
Employee2=Employee(2000,"Hala Rana ","Aqaba ,Joradan",750,"Deparment Manager",[150,3000,250])
Employee3=Employee(3000,"Mariam Ali ","Mafraq,Joradan",600,"HR's consultant",[304,1000,250,300,500,235])
Employee4=Employee(4000,"Yasmeen Mohammad ","Karak,Joradan",865,"Director",[])
EmployeeList.append(Employee1)
EmployeeList.append(Employee2)
EmployeeList.append(Employee3)
EmployeeList.append(Employee4)

def numberofEmployee (EmployeeList):
    print(len(EmployeeList))


def infofEmployee(EmployeeList):
    for index,Employee in enumerate( EmployeeList):
        print(EmployeeList[index].infoEmployee())
        
def minloan(EmployeeList):
    minlist=[]
    for index,Employee in enumerate( EmployeeList):
         if type(EmployeeList[index].loansmin())==int:
            minlist.append(EmployeeList[index].loansmin())
    print (min(minlist))
    
    
def maxloan(EmployeeList):
    maxlist=[]
    for index,Employee in enumerate( EmployeeList):
         if type(EmployeeList[index].loansmax())==int:
            maxlist.append(EmployeeList[index].loansmax())
    print (max(maxlist))    


def listofloan(EmployeeList):
     totallist=[]
     result=0
     for index,Employee in enumerate( EmployeeList):
            totallist.append(EmployeeList[index].getloans())
            totallist.append(EmployeeList[index].loanstotal())
     for index,Employee in enumerate( EmployeeList):
         result=EmployeeList[index].loanstotal()+result
         
     totallist.append(result)
     print (totallist)
    
    


def loanDic(EmployeeList):
    loanDic={}
    for index,Employee in enumerate( EmployeeList):
         loanDic[ EmployeeList[index].number]=EmployeeList[index].getloans()
    print(loanDic)
    return (loanDic)
       
result=loanDic(EmployeeList)

def lowestMaxloan(result):
    
    for key in result:
        if(len(result[key]))>0:
            print (functools.reduce(lambda a,b : a if a> b else b,result[key]))
        else:   
            print("No_max_loan")
            
    for key in result:
        if(len(result[key]))>0:
            print (functools.reduce(lambda a,b : a if a< b else b,result[key]))
        else:   
            print("No_Mini_loan")     
            
            


def hightssalary(EmployeeList):
     maxsalary=[]
     for index,Employee in enumerate( EmployeeList):
         maxsalary.append(EmployeeList[index].getsalary())
     print(max(maxsalary))
     

def lowestsalary(EmployeeList):
     minsalary=[]
     for index,Employee in enumerate( EmployeeList):
         minsalary.append(EmployeeList[index].getsalary())
     print(min(minsalary))


def totaltsalary(EmployeeList):
     totalsalary=0
     for index,Employee in enumerate( EmployeeList):
         totalsalary=EmployeeList[index].getsalary()+totalsalary
     print(totalsalary)
def dellist(EmployeeList): 
    for index,Employee in enumerate(EmployeeList):
        
            print (EmployeeList[index].__del__())  
            


#Q3
numberofEmployee(EmployeeList)          
# Q5=============================================================================
# infofEmployee(EmployeeList)
# =============================================================================
 
          
# =============================================================================
# Q14
#hightssalary(EmployeeList)
#Q15
# lowestsalary(EmployeeList)
#Q16
# totaltsalary(EmployeeList)
# 

#Q11
# loanDic(EmployeeList)
#Q12
# lowestMaxloan(result)  
# 
# 
#Q10  
# listofloan(EmployeeList)  
#Q9 
# maxloan(EmployeeList)   
#     
#Q8 
#minloan(EmployeeList)
#Q17
#dellist(EmployeeList)
# =============================================================================

      



# Q2
StudentList=[]
Student1=Student(20191000,"Khaled Ali","irbid,Jordan","History",{"English":80,"Arabic":90,"Art":95,"managment":75})
Student2=Student(20182000,"Reem Hani","Zarqa,Jordan","Softawre eng",{"English":80,"Arabic":90,"calculas":85,"managment":75,"OS":73,"Programming":90})
Student3=Student(20161001,"Nawras Abdallah","Amman,Jordan","Art",{"English":83,"Arabic":92,"Art":90 ,"managment":70})
Student4=Student(20172030,"Amal Raed","Tafielh,Jordan","Computer eng",{"English":83,"Arabic":92,"calculas":80,"managment":70,"OS":79,"Programming":91})
#
StudentList.append(Student1)
StudentList.append(Student2)
StudentList.append(Student3)
StudentList.append(Student4)
# =============================================================================

def numberofStudent(StudentList):
    print(len(StudentList))
def infEmployee(StudentList):
    for index,student in enumerate( StudentList):
        print(StudentList[index].print_info())
        
def maxavg(StudentList):
    maxlist=[]
    for index,Student in enumerate(StudentList):
        maxlist.append(StudentList[index].Average())
    print (max(maxlist))    


def MarkA(StudentList):
  for index,Student in enumerate(StudentList):
        if StudentList[index].MarkofA()>0:
            print (StudentList[index].print_info())  
            
       
def dellists(StudentList): 
     for index,Student in enumerate(StudentList):
        
             print (StudentList[index].__del__())
    
# =============================================================================
#         print (StudentList+'I have been deleted') 
# =============================================================================
#Q17 
#dellists(StudentList) 
# =============================================================================
# Q13
#MarkA(StudentList)         
#Q7 
#maxavg(StudentList)
# #
#Q6
# infEmployee(StudentList)      
#Q4 
#numberofStudent(StudentList)
# =============================================================================

