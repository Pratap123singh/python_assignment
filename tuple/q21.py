# 21. Write a Python program to replace the last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
l1=list()
l1=[l1[:2:] + (100,) for l1 in l]
print(l1)

l4=list()
for e in l:
     ll=list(e)
     ll[2]=100
     tt=tuple(ll)
     l4.append(tt)
print(l4)

for e in l:
    ll=list(e)
    ll.insert(2,100)
    ll.pop()
    tt=tuple(ll)
    l4.append(tt)
print(l4)
