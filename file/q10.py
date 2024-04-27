# # 10. Write a Python program to count the frequency of words in a file.

with open("file.txt","r") as f:
    x=f.read()
    y=x.replace("\n",".")
    z=y.replace(" ",".")
    l1=z.split(".")
    dict1=dict()
    for e in l1:
        c=l1.count(e)
        dict1[e] = c
print(dict1)

