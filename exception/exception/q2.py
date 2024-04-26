
# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception
#  if the input is not a valid integer.
def value_error_handling():
    try:
        x=int(input("enter a number: "))
        print(x)
    except ValueError:
        print("Plase enter integer number.")
    else:
        print("inside else")
    finally:
        print("inside finally")

value_error_handling()