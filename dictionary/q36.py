# 36. Write a Python program to create a dictionary from two lists without losing duplicate values.

l1=[1,2,3,4,5,6]
l2=[10,20,30,30,40,30]
d=dict()
for idx in range(0,len(l1),1):
    d[l1[idx]]=l2[idx]

print(d)
