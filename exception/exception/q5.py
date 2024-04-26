# 5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.

try:
    with open('folder1') as f:
        print(f.read())
except FileNotFoundError:
    print("file does not exist.")
except PermissionError:
    print("inside PermissionError.")
else:
    print("inside else")
finally:
    print("inside finally")
