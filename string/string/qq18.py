# 18. Write a Python function to get a string made of the first three characters of a
# specified string. If the length of the string is less than 3, return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt

def first_three(s: str):
    if len(s)>3:
        return s
    else:
        return s[0:3:1]
print(first_three("python"))
print(first_three("pyt"))
print(first_three("py"))


