#Q Sort all the characters of given string using lambda function

str1="i love my country."

l=sorted(str1, key=lambda x : x)
print(l)
s=""
for e in l:
    s=s+e
print(s)