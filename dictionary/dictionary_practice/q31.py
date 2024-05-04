# 31. Write a Python program to get the key, value and item in a dictionary.
d = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
for k,v in d.items():
    print(k, v)
d1=dict()
l=list(d.items())
for e in l:
    d1[e[0]]=e[1]
    print(d1)
    d1.clear()
