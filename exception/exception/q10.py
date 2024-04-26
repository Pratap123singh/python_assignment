# 10. Write a Python program that executes a list operation and handles an AttributeError exception
# if the attribute does not exist.

i=10
try:
    i.append(20)
except AttributeError:
    print("inside AttributeError")
else:
    print("inside else")
finally:
    print("inside finally")
