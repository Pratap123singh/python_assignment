# 6. Write a Python program to read a file line by line store it into a variable.

with open("x_file", "r") as f:
    l=f.readlines()
    print(l)

s1=l[0]
s2=l[1]
print(f"s1: {s1}")
print(f"s2: {s2}")

#l=[1,2,3]
#print(l[0:2:1])