# 24. Write a Python program to check whether a string starts with specified
# characters.(do both using library and without library)

str1="hello hello"

def s_start(s: str):
    idx = str1.find(s,0,len(str1))
    if idx == 0:
        print("yes, string starts with specified character.")
    else:
        print("no, string do not starts with specified character.")
    
    if str1[0:1:1] == s:
        print("yes, string starts with specified character.")
    else:
        print("no, string do not starts with specified character.")

s_start("h")

