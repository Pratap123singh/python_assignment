# Q. Take comma separated numbers as input from the user. Split it in list of strings. 
# Now convert every string in this list to 
# float using map function

str1="1,2,3,5.5"
list1=str1.split(",")
print(list1)
res=map(float, list1)   #<map object at 0x000001E6CDB739A0>
#print(res)
list2=[]
for i in res:
    #print(i)
    list2.append(i)
print(list2)
