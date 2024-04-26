# 7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception 
# if the user cancels the input.

try:
    x=float(input("enter salary: "))
    print(x)
except KeyboardInterrupt:
    print("\ninside keyboardInterrupt. You pressed ctrl + C ")
except ValueError:
    print("inside value error. You have enter a string instead of float.")
else:
    print("inside else")
finally:
    print("inside finally")
  