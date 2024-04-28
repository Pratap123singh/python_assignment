# 11. Write a Python program to remove characters that have odd index values in a given string.

str1="hello, how are you?"
s2=str()
#print(len(str1))
for idx in range(0,len(str1),1):
    if idx%2 == 0:
        s1=str1[idx:idx+1:1]
    s2 = s2 + s1
    s1=""

print("str2: ", s2)

