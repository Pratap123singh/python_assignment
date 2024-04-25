#if we write only except: 
def divide(num1: int, num2: int):
    try:
        print("above")
        result = num1//num2
        print("below")
        #print(f"result: {result}")
        return result
    except:
        print("write only except.")
    else:
        print("inside else")
    finally:
        print("inside finally")
    
    print("after try-except block")
    
print(divide(10,0))
