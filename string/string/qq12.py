# 12. Write a Python program to count the occurrences of each word in a given sentence.

str1="Hello i am a wonderful hello Hello person person"

l=list(str1.split( ))
dict1=dict()
dict2=dict()
for e in l:
    count=l.count(e)
    dict1[e]=count

print(dict1)

for char in list(str1.split()):
    count=list(str1.split()).count(char)
    dict2[char]=count
print(dict2)
