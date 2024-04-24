# 9. Write a Python program to remove the nth index character from a nonempty string.

str1="abccvcv"
x=int(input("enter index: "))
def _remove(s : str, n: int):
    sub1=s[0:n:1]
    sub2=s[n+1:len(s):1]
    new_string = sub1 + sub2
    
    return new_string

print(_remove(str1,x))
