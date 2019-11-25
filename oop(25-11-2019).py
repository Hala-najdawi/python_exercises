class Employee:
     def __init__(self,number,name,address,salary,job_title):
        self.number=number
        self.__name=name
        self.__address=address
        self.__salary=salary
        self.__job_title=job_title
     def getName(self):
         return self.__name
     def getAddress(self):
         return self.__address
     def getSalary(self):
         return self.__salary
     def getjobTitle(self):
         return self.__job_title
     def setAddress(self,address):
          self.__address=address
     def __del__(self):
         print (self.__name,"has been deleted")
     def print_info(self):
               print(f'''
                         number:{self.number}
                         Name:{self.__name}
                         Address:{self.__address}
                         Salary:{self.__salary}
                         Job_title:{self.__job_title} 
                         ''')
     def print_info_2(self):
               print(f'''number:{self.number},Name: {self.__name},Address: {self.__address},Salary: {self.__salary},Job_title:{self.__job_title}''')
employee1=Employee(1,"Mohammad Khalid","Amman Jordan",500,"consultant")
employee2=Employee(2,"Hala Rana","Aqaba Jordan",750,"Manager") 
employee1.print_info()
employee1.setAddress("USA") 
print('Employee1 New Address : ' + employee1.getAddress())
del employee1
del employee2