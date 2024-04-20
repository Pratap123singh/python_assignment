# Write a Python program to check whether an element exists within a tuple.

#t1=(10,20,(200,"hi"),["hello", 210],20,(200,"hi"))
#print(type(t1))
#print(t1)

t2=(10,20,30,40)
print(type(t2))
print(t2)
m=int(input("enter an element: "))
#print(type(m))
for e in t2:
    if e == m:
        print("element exist inside a tuple")
        