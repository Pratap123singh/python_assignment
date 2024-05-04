# 46. Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}

l=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
l1=list()
d=dict()
print(l[0][0])
print(l[0][1])
r=[e[0] for e in l]
print("r: ", r)
for idx in range(0,len(l),1):
    val1 = l[idx][1]
    key1 = l[idx][0]
    for k in r:
        if key1 == k:
            print("val1: ", val1)
            l1.append(val1)
        print(l1)
    #d[key1]=l1

print(d)