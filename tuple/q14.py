#14. Write a Python program to find the index of an item in a tuple.
t=(10,20,30,40,50,40,60,70)

x=int(input("enter number: "))

for idx in range(0,len(t),1):
    if x == t[idx]:
        print(f"index of {x}: ", end="")
        print(idx)
