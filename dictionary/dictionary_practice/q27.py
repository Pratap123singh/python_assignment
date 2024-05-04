# 27. Write a Python program to convert a list into a nested dictionary of keys.

# Ex. i/p [1, 2, 3, 4]
# o/p  {1: {2: {3: {4: {}}}}}

l=[1,2,3,4]
a=d=dict()
for e in l:
    d[e]={}
    d=d[e]
print(a)