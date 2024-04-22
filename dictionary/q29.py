# 29. Write a Python program to remove spaces from dictionary keys.
# After removing spaces if keys repeat then keep the latest value.
# Ex. 
# i/p
# {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English'], 'S 3':['Math', 'English'], 'S3':['English'], }
# o/p
# {'S001': ['Math', 'Science'], 'S002': ['Math', 'English'], 'S3':['English']}

d={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English'], 'S 3':['Math', 'English'], 'S3':['English']}
d1=dict()

def remove_spaces(k: str):
    str1=k.replace(" ","")
    return str1

for k,v in d.items():
    # str2=remove_spaces(k)
    # d1[str2]=v
    d1[remove_spaces(k)]=v
print(d1)