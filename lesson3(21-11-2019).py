
#EX1:Write a Python program to print each item in a list in new line.
"""
list=[1,2,3,4,5,6]
for itemlist in list:
    print(itemlist)
"""    
#EX2:Write a Python program to sum all the items in a list and print the sum.
"""
list=[1,2,3,4,5,6]  
print("sum all the items in a list=",sum(list))
"""
#EX3:Write a Python program to get the largest number from a list.
"""
list3=[10,-2,44,9,5,3]
print("The Largest numder:",max(list3))
"""
#EX4:Write a Python program to remove duplicates from the following list
"""
a=[10,20,30,20,10,50,60,40,80,50,40]
print(list(set(a)))
"""
#EX5:Write a Python program to check a list is empty or not
"""
list5=[1,8,0,4,77,100]
if len(list5)>0:
    print("the list is not empty")
else:print("the list is empty")
"""
#EX6:Write a Python program to create a tuple with different data types and print each item in a new line
"""
tuples=("H","A","L","A")
for x in tuples:
    print(x)
"""
#EX7:Write a Python program to iteration over sets, use the set num_set = set([0, 1, 2, 3, 4, 5])
"""
num_set = set([0, 1, 2, 3, 4, 5])
for set in num_set:
    print(set)
"""
#EX8:intersection
"""
set1={"ford","BMW"}
set2={"Audi","GMC","BMW"}
print ( set1 & set2 )
"""
#EX9:Write a Python program to create an intersection of sets.
"""
setx=set(["green", "blue"])
sety=set(["blue", "yellow"])
seta=setx | sety
print(seta)
"""
#EX10:OUTPUT
"""
seta=set([5,10,3,15,2,20])
print(len(seta))
"""
#EX11:OUTPUT
"""
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1,dic2,dic3):
    dic4.update(d)
print(dic4)
"""
#EX11:OUTPUT
a="Hello,world!"
print(a[1])#output:e
print(a[2:5])#output:llo
print(a[-5:-2])#output:orl
print(len(a))#output:12
print(a.lower())#output:hello,world!
print(a.replace("H","J"))#OUTPUT:Jello,world!
