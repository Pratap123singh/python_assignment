# 4. Write a Python program to read last n lines of a file.
x=int(input("enter line number: "))
with open("file.txt", "r") as f:
    for line in (f.readlines()[-x:]):
        print(line,end="")
