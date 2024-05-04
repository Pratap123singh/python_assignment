#11. Write a Python program to multiply all the items in a dictionary.

d1={1:10, 2:20, 3:30}
mul=1
for e in d1.items():
    mul*=e[1]
print("Multiple of all the item in a dictionary: ", mul)