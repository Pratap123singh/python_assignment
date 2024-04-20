#16. Write a Python program to convert a tuple to a dictionary.
t=(10,20,30,40,50,40,60,70)
d=dict()
for idx in range(0,len(t),1):
    d[idx]=t[idx]
print(type(d))
print(d)