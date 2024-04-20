#19. Write a Python program to convert a list of tuples into a dictionary.

l=[(10,20),(30,40),(50,70)]
d=dict()
for idx in range(0,len(l),1):
    d[l[idx][0]]=l[idx][1]
print(d)