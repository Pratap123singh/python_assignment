# 28. Write a Python program to convert a tuple of string values to a tuple of integer values.
# Original tuple values:
# (('333', '33'), ('1416', '55'))
# New tuple values:
# ((333, 33), (1416, 55))

t=(('333', '33'), ('1416', '55'))
t1=t2=()
for e in t:
    l=[]
    for e1 in e:
        i=int(e1)
        l.append(i)
        t1=tuple(l)
    t2=t2+(t1,)
print(t2)
        