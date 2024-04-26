# 8. Write a Python program that executes division and handles an ArithmeticError exception 
# if there is an arithmetic error.
import math

try: 
    result=math.exp(1000)
except OverflowError:
    print("inside overflowError. overflowError is child of Arithmetic error.")
else:
    print("inside else.")
finally:
    print("inside finally.")

