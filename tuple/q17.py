#17. Write a Python program to unzip a list of tuples into individual lists.
t=(10,20,30,40,50,40,60,70)
l=[(10,20),(30,40),(50,70)]
a,*b,c=l
print(list(a))
print(*b)
print(list(c))

