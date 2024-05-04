# 24. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

str1 = 'w3resource'
l1=list(str1)
d=dict()
for e in l1:
    d[e]=l1.count(e)
print(d)
