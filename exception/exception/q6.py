# 6. Write a Python program that executes an operation on a list and handles an IndexError exception
# if the index is out of range.

l=[1,2,3,4]


try:
    for idx in range(0,6,1):
        print(l[idx])
except IndexError:
    print("list index out of range")
else:
    print("inside else")
finally:
    print("inside finally")

