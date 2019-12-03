#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:11:35 2019

@author: owner
"""
#EX1:
"""
from sympy import *
from sympy.plotting import *
x,y,z = symbols('x y z')
#a-
expr= x**2+x**3+21*x**4 + 10*x+1
print( expr.subs(x, 7) )
#b-
print(expand( (x + y) ** 2))
#c-
print(simplify(4*x**3+21*x**2+10*x+12))
#d-
print(limit(1/(x**2),x,oo))
#e
print(summation(2*i+i - 1, (i, 5, n)))
#f-
print(integrate(sin(x)+exp(x)*cos(x)+tan(x),x))
#g-
print(factor(x**3 + 12*x*y*z +3*y**2*z) )
#h-
print(solveset(x-4,x))
#i-
m1 =Matrix([[5, 12, 40], [30, 70, 2]])
m2 =Matrix([2, 1, 0])
print( m1*m2 )
#j-
plot(x**3+3, (x, -10, 10))
#k-
f=x**2*y**3
plot3d(f, (x, -6, 6), (y, -6, 6))
"""
#EX2:
"""
import xlsxwriter
workbook=xlsxwriter.Workbook("EX2.xlsx")
worksheet=workbook.add_worksheet()
worksheet.autofilter('A1:B1')
data=["This is example"]
format=workbook.add_format()
format.set_bold()
format.set_font_size(12)
format.set_font_color("red")
worksheet.write_column("A1:B1",data,format)
data1=["export my sheet"]
format=workbook.add_format()
format.set_bold()
format.set_font_size(12)
worksheet.write_column("A2:B2",data1,format)
data2=[1,2]
format=workbook.add_format()
format.set_font_size(12)
worksheet.write_column("A3:B4",data2,format)
data3=[3]
format=workbook.add_format()
format.set_font_size(12)
format.set_bold()
format.set_font_color("red")
worksheet.write_column("A5",data3,format)
workbook.close()
"""
#EX3:
from xlrd import open_workbook
wb = open_workbook('Hala.xlsx')
for s in wb.sheets():
     print ("Sheet:", s.name)
     for row in range(s.nrows):
         values = []
         for col in range(s.ncols):
           values.append(s.cell(row,col).value)
         print(','.join(values))