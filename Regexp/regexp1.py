import re

str1 = "ramesh r ramu a7mu7 h"
result1=re.search("ramu",str1)
print(result1)
try:
    print(result1[0])
    print(result1.span())
except TypeError:
    print("handling error")

