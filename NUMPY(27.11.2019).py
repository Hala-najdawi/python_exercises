#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 12:48:44 2019

@author: owner
"""
import numpy as np
#ex1:
"""
e= np.zeros( (4,10) )
print (e)
e= np.ones( (4,10) )
print (e)
e= np.ones( (4,10) )*5
print (e)
"""

#EX2
"""
array=np.arange(30,70)
print("Array of all the integers from 30 to 70")
print(array) 
"""
#EX3
"""
import numpy as np
array=np.arange(30,71,2)
print("Array of all the even integers from 30 to 70")
print(array)
"""
#EX4
"""
A =np.identity(3)
print(A) 
"""
#EX5
"""
array=np.random.normal(0,1,1)
print("Array of all the integers from 0 to 0")
print(array) 
"""
#EX6
"""
a = np.arange(12).reshape(3, 4)
print(a)
for x in np.nditer(a):
    print(x,end=" ")
"""
#EX7
"""
import numpy as np
x = np.arange(20)
print("Original vector:")
print(x)
print("After changing the sign of the numbers in the range from 9 to 15:")
x[(x >= 9) & (x <= 15)] *= -1
print(x)
"""
#EX8:
"""
x=[1,8,3,5]
y=np.random.randint(0,11,4)
result = x * y
print("Multiply the values of two said vectors:")
print(result)
"""
#EX9
"""
a=np.arange(10,22).reshape((3, 4))
print(a)
print ("Number of rows and columns of the said matrix:", a.shape)
"""
#EX10
"""
x = np.random.random((3, 3, 3))
print(x)
"""
#EX11
"""
a=np.array([9,-1,2,5])
b=np.array([1,-6,0,10])
c=np.array([[1,8,2,5],[3,1,7,9]])
print("a-b:",a-b)
print("a*b:",a*b)
print("a.dot(b):",a.dot(b))
print("a*2:",a*2)
print("np.sin(a):",np.sin(a))
print("a<3:",a<3)
print("a.sum():",a.sum())
print("a.sum(axis=0):",a.sum(axis=0))
print("c.sum():",c.sum())
print("c.sum(axis=0):",c.sum(axis=0))
print("a.min():",a.min())
print("a.max():",a.max())
print("a.mean():",a.mean())
print("a.average():",np.average(a))
print("a.median():",np.median(a))
print("a.std():",np.std(a))
print("a.var()",np.var(a))
print("c.cumsum():",c.cumsum())
print("a[1:2]:",a[1:2])
print("a[2:]:",a[2:])
print("c[-1]:",c[-1])
"""
#EX12
"""
import matplotlib.pyplot as plt
X = range(1, 50)
Y = [value * 3 for value in X]
plt.plot(X, Y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line.')
plt.show()
"""
#EX13:
"""
import matplotlib.pyplot as plt
x1 = [10,20,30]
y1 = [20,40,10]
plt.plot(x1, y1, label = "line 1")
x2 = [10,20,30]
y2 = [40,10,30]
plt.plot(x2, y2, label = "line 2")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines on same plot with suitable legends ')
plt.legend()
plt.show()
"""
#EX14

t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'g--', t, t**2, 'bs', t, t**3, 'r^')
plt.show()

#EX 15:
import matplotlib.pyplot as plt
x = ['Python', 'Java', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language")
plt.xticks(x_pos, x)
#
plt.show()
#
# 