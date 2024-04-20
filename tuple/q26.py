# 26. Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
# Original Tuple:
# (4, 3, 2, 2, -1, 18)
# Product - multiplying all the numbers of the said tuple: -864
# Original Tuple:
# (2, 4, 8, 8, 3, 2, 9)
# Product - multiplying all the numbers of the said tuple: 27648
t=(4, 3, 2, 2, -1, 18)
t1=(2, 4, 8, 8, 3, 2, 9)
print("\n",t[0])
mul=1
for e in t:
    mul*=e
print(f" Product - multiplying all the numbers of the said tuple: {mul}")
mul1=1
for e in t1:
    mul1*=e
print(f" Product - multiplying all the numbers of the said tuple: {mul1}")
