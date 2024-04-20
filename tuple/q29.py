# 29. Write a Python program to convert a given tuple of positive integers into an integer.
# Original tuple:
# (1, 2, 3)
# Convert the said tuple of positive integers into an integer:
# 123
# Original tuple:
# (10, 20, 40, 5, 70)
# Convert the said tuple of positive integers into an integer:
# 102040570

t=(1, 2, 3)
t2=(10, 20, 40, 5, 70)
l=[]
for e in t2:
    i=int(e)
    l.append(i)
s=""
for e in l:
    s1=str(e)
    s=s+s1
#print(s)
int1=int(s)
print(int1)
