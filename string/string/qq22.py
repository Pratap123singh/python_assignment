# 22.Write a Python program to sort a string lexicographically.(do both using library and without library)

str1="red, green, blue, white, black"

for char in str1.split():
    s=char
    if char > s:
        print("yes")
        