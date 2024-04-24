# 2. Write a Python program to get character frequency of every character in a string.
# Sample String : google.com
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

str1= "google.com.com"
dict1=dict()
v=list()
k=list()

def frequency_count(s: str):
    for e in str1:
        v.append(str1.count(e))
        k.append(e)
    return (k,v)
   
def create_dictionary_from_list(l1: list, l2: list):
    for idx in range(0,len(l1),1):
        dict1[l1[idx]] = l2[idx]
    return dict1
  
result=frequency_count(str1)
print(create_dictionary_from_list(result[0],result[1]))



