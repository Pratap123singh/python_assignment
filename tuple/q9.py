#Write a Python program to find repeated items in a tuple.
t=(1,7,4,7,4,5,5,5,6)

l2=list(t)
print("l2: ", l2)
l3=[]
for idx in range(0,len(t),1):
    count1=l2.count(l2[idx])
    if count1 >= 2:
        l3.append(l2[idx])

set1=set(l3)
t2=tuple(set1)
print(t2)    

