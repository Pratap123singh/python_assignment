#18. Write a Python program to check if a dictionary is empty or not.

d1={1:10, -2:20, 3:30, -4:40, 5:30, 6:30}
d2={}
print(len(d1))
print(len(d2))

if len(d2)==0:
    print("dictionary is empty")
else:
    print("dictionary is not empty")
    