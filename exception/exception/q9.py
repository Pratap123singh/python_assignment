# 9. Write a Python program that opens a file and handles a UnicodeDecodeError 
# exception if there is an encoding issue.
try:
    with open("sample_file_1.txt") as f:
        print(f.read())
except UnicodeDecodeError:
    print("inside UnicodeDecodeError.")
else:
    print("inside else.")
finally:
    print("inside finally.")