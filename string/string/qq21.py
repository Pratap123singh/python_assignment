# 21. Write a Python function to convert a given string to all uppercase if it contains
# at least 2 uppercase characters in the first 4 characters.

def upper_2(s: str):
    count=0
    for char in s[0:4:1]:
        if char.isupper() == True:
            count+=1
    if count >= 2:
        return s.upper()
    else:
        return s

print(upper_2("HEllo"))
print(upper_2("Hello"))
print(upper_2("HooloLL"))
