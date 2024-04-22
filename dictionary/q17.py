#17. Write a Python program to remove duplicates from the dictionary.

d1={1:10, -2:20, 3:30, -4:40, 5:30, 6:30}

print(d1)
d2=dict()
for k,v in d1.items():
    print(k,v)
    if v not in d2.values():
        d2[k]=v
print(d2)

