def divide(num1: int, num2: int):
    try:
        print("above")
        result = num1//num2
        print("below")
        print(f"result: {result}")
        #return result
    except ZeroDivisionError:
        print("Divide by zero error. Please do not pass zero in denominator.")
    else:
        print("if no exception then control goes to else")
    
    print("execution continue after try-except block")
    
divide(10,0)
