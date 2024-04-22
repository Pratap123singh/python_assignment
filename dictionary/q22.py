#22. Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

d1={1:10, 2:20, 3:30, 4:10, 5:90, 6:99}
l=list()
for v in d1.values():
    l.append(v)
#print(l)
ll=sorted(l, key= lambda x : x, reverse=True)
#print(ll)
print(ll[0:3:1])