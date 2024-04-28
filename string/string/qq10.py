# 10. Write a Python program to change a given string to a newly
# string where the first and last chars have been exchanged.

str1="Hello i awesome person"

s1=str1[0:1:1]
s2=str1[-1]
result = s2 + str1[1:len(str1)-1:1] + s1

print(result)