# 2. Write a Python program to read first n lines of a file.
n=int(input("enter no. of lines to read: "))
with open("file.txt") as f:
    first_line = f.readlines()
    #print(first_line)
    # for line in first_line:
    #     print(line)
    for idx in range(0,n,1):
        print(first_line[idx])