# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string 
#is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

str1="ningging"

def add_suffix(s: str):
    result=str()
    if len(s) > 3 and s.endswith("ing",len(s)-3,len(s)) != True:
        result = s + "ing"
    elif len(s) > 3 and s.endswith("ing",len(s)-3,len(s)) == True:
        result = s.replace(s[-3:],"ly")
    elif len(s) < 3:
        result = s
    return result

print(add_suffix(str1))
