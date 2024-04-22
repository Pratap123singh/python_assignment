# 32. Write a Python program to print a dictionary line by line.
# Ex. 
# i/p {'S001': ['Math', 'Science'], 'S002': ['Math', 'English'], 'S3':['English']}
# o/p 
# 'S001':['Math', 'Science']
# 'S002':['Math', 'English']
# 'S3':['English']

d={'S001': ['Math', 'Science'], 'S002': ['Math', 'English'], 'S3':['English']}
d1=dict()
l=list(d.items())
for e in l:
    d1[e[0]]=e[1]
    print(d1)
    d1.clear()

    