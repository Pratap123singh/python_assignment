# 31. Write a Python program to compute the element-wise sum of given tuples.
# Original lists:
# (1, 2, 3, 4)
# (3, 5, 2, 1)
# (2, 2, 3, 1)
# Element-wise sum of the said tuples:
# (6, 9, 8, 6)

t1=(1, 2, 3, 4)
t2=(3, 5, 2, 1)
t3=(2, 2, 3, 1)
t=((1, 2, 3, 4),(3, 5, 2, 1),(2, 2, 3, 1))

for i in range(0,2,1):
    s1=0
    for e in t:
        print(e[i])
        s1+=e[i]
        tt=(s1,)
    continue
print(s1)
print(tt)

