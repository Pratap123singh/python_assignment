# 5. Write a Python program to read a file line by line and store it into a list.

with open("file.txt", "r") as f:
    #print(type(f.read()))
    #print(f.read())
    l = f.readlines()
    #print(type(l))
    print(l)
    
