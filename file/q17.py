# 17. Write a Python program to remove newline characters from a file.

def file1(file_name):
    with open(file_name,"r") as f:
        x=f.read( )
        y=x.replace("\n",".")
        print(y)

file1("file.txt")
