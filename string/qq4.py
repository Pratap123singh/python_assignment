# 4. Write a Python program to get a string from a given string where all occurrences of its 
# first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'
# Sample String : 'ababab'
# Expected Result : 'ab$b$b'

str1="ababab"
str2=str1[1:len(str1):1]
substring=str1[0:1:1]

def f1(s: str, sub: str):
    for e in s:
        result=s.replace(sub, "$")
    return sub+result
print(f1(str2,substring))