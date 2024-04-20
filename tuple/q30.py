# 30. Write a Python program to check if a specified element appears in a tuple of tuples.
# Original list:
# (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
# Check if White presenet in said tuple of tuples!
# True
# Check if White presenet in said tuple of tuples!
# True
# Check if Olive presenet in said tuple of tuples!
# False

t = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))

x=input("enter element: ")

for e in t:
    for e1 in e:
        if x == e1:
            print("x: ", x)
            print("e1: ", e1)
            print("True")
            break 
else:
    if x != e1:
        print("x1: ", x)
        print("e11: ", e1)
        print("False")
