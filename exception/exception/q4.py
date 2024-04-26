# 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if 
# the inputs are not numerical.

x=input("enter a number: ")
y=input("enter a number: ")

def subtraction(num1: int, num2: int):
    try:
        result = num1 - num2
        return result
    except TypeError:
        print("inside type error")
    else:
        print("inside else")
    finally:
        print("inside finally")

print(subtraction(x,y))