#12. Write a Python program to remove a key from a dictionary.

d1={1:10, 2:20, 3:30}
print(d1)
x=int(input("enter a key: "))
del d1[x]
print(d1)