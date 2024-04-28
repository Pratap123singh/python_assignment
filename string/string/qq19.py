# 19. Write a Python program to get the last part of a string before a specified character.
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python

str1="https://www.w3resource.com/python-exercises"

def last_part(s_char:str, s:str):
    s1 =str()
    print(s.partition(s_char))
    for e in s.partition(s_char)[::-1]:
        s1 = s1 + e
        break
    print(s1)

last_part("-",str1)
