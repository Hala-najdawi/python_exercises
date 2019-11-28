#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:23:06 2019

@author: owner
"""

#EX1:
"""
import pandas as pd
data = [100, 120, 140, 180, 200, 210, 214]
s = pd.Series(data)
"""
#EX2:
"""
import pandas as pd
d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
s=pd.Series(d1)
print(s)
"""
#EX3:
"""
import pandas as pd
data = [20, 10, 150, 110, 100, 50]
s=pd.Series(data)
print( s.describe())
s.plot(kind="bar",color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])
"""
#EX4:
"""
import pandas as pd
Data = {'d1':[100,200,5,400,700,100,200,50,400,700],
'd2':[140,0,300,400,200,140,0,700,400,200]}
df = pd.DataFrame(Data,columns=["d1", "d2"])
df.plot()
"""
#EX5:
"""
import pandas as pd
data={
'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
data=pd.DataFrame(data)
print ( data )
"""
#EX6:
"""
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]
series = pd.Series(births, index=names, name='series')
series.plot.pie(y='births', figsize=(5, 5))
"""
#EX7:
# =============================================================================
# """
# import pandas as pd
# d = [100,2200,300,400,500,600,700,800,900]
# df = pd.DataFrame(d, columns = ['Number'])
# df.to_csv('myDataFrame.csv', sep='\t')
# df =pd.read_csv('myDataFrame.csv',sep='\t',index_col=0)
# print(df)
# df =pd.read_csv('myDataFrame.csv',sep=',',index_col=0)
# print(df)
# """
# =============================================================================
#EX8


import pandas as pd
import numpy as np
dates =pd.date_range('20000101', periods=4)
df= pd.DataFrame(np.random.randn(4, 2), index=dates, columns=["A","B"])
print(df)
print("----------------------------------------")
print(df.head(2))
print("----------------------------------------")

print(df[['A']])
print("----------------------------------------")

print(df[0:1]) 
print("----------------------------------------")

print(df['20000102':'20000104'])
print("----------------------------------------")

print(df.loc['20000102':'20000104', ["A"]])
print("----------------------------------------")

print(df.iloc[:,1:2])
print("----------------------------------------")

print(df[df>0])
print("----------------------------------------")

print(df[df.B>0])
print("----------------------------------------")

df["A"]=[100,200,300,100]
print(df)
print("----------------------------------------")

print(df[df['A'].isin([200,300])])