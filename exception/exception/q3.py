# 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

try:
    with open("sample_file_1.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File does not exist.")
else:
    print("inside else")
finally:
    print("inside finally")

