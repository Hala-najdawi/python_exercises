#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:19:24 2019

@author: owner
"""
#EX1:What is the outcome from this program
"""
o=lambda x=1,y=2,z=3:x+y+z
print(o())
print(o(10))
print(o(10,20))
"""
#EX2:Write a Python function to multiply the numbers in list
"""
from functools import reduce
print(reduce(lambda a,b : a*b,[2,3]))

"""
#EX3:lambda function that multi plies:
"""
from functools import reduce
x= reduce(lambda a,b: a*b,[2,3,2])
print(x) 
"""
#EX4:Lambda,filter to return a list negative numbers
"""
x=list(filter(lambda a : a <0 ,range(-5,5)))
print(x)
"""
#EX5:What IS the outcome
"""
x=lambda a,b,c:a+b+c
print(x(5,6,2))
"""
#EX6:What is the outcome
"""
x=("Joey","Monica","Ross")
y=("Chandler","Pheobe")
z=("David","Rachel","Counrtney")
result=list(zip(x,y,z))
print(result)
"""
#EX7:What is the outcome
"""
coin=('bitcoin','ether','ripple','litecoin')
code=('btc','eth','xrp','ltc')
d=dict(zip(coin,code))
print(d)
"""
#EX8:What is the outcome
"""
def fun(variable):
    letters=['a','e','i','o','u']
    if(variable in letters):
        return True
    else:
        return False
sequence=['g','j','e','j','k','o','p','r']
filtered=list(filter(fun,sequence))
print(filtered)
"""
#EX9:What is the outcome
"""
x=list(map(int,input("Enter a multiply value:").split()))
print("list of student:",x)
"""
#EX10:What is the outcome
"""
def newfunc(a):
    return a*a
x=list(map(newfunc,(1,2,3,4)))
print(x)
"""
#EX11:What is the outcome
"""
def func(a,b):
    return a+b
a=list(map(func,[2,4,5],[1,2,3,2,4]))
print(a)
"""
#EX12:What is the outcome
"""
c=map(lambda x:x+x,filter(lambda x:(x>3),(1,2,3,4)))
print(list(c))
"""
#EX13:What is the outcome
"""
c=filter(lambda x:(x>=3),map(lambda x:x+x,(1,2,3,4)))
print(list(c))
"""
#EX14:write a python program to get the minimum value in the list using reduce
import functools
lis = [ 1 , 3, -5, 6, 2]
print ("The minimum element of the list is : ",end="")
print (functools.reduce(lambda a,b : a if a < b else b,lis))
#EX15:Write a python program to convert the following list into tuples using zip
numbers=[1,2,3]
letters=['a','b','c']
results =tuple(zip(numbers,letters))
print(results)