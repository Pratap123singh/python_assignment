def prime(x: int):
    if x > 1: 
        m=2
        while(m<(x//2 + 1)):
            if x%m == 0:
                print(f"{x} is not prime")
                break
            m+=1
        else:
                print(f"{x} is prime")
    else:
        print("Not valid input")
num=int(input("enter a number: "))
prime(num)
