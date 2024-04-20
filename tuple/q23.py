# 23. Write a Python program to sort a tuple by its float element.
# Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

l= [('item1', '12.20'), ('item2', '-15.10'), ('item3', '24.5')]
d=dict(l)
#print(d)
k=sorted(d.items(), key = (lambda x : x[1]), reverse=True)
#print(k)
l1=list(k)
print(l1)
