# 26. Write a Python program to count the values associated with a key in a dictionary.
# Expected Output:
# 6
# 2
print("\n")
d={1:[1,2,3,4,5,6], 2:[1,2,3], 3:123}

for e in d.values():
    count=0
    if isinstance(e,list) == True:
        for i in e:
            count+=1
    else:
        count=1
    print(count)
