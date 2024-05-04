#13. Write a Python program to map two lists into a dictionary.

l1=[10,20,30,(25,50)]
l2=[58,'sita',20,'ram']
print((zip(l1,l2)))
print(dict(zip(l1,l2)))
print(tuple(zip(l1,l2)))
print(list(zip(l1,l2)))