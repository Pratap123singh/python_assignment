# Q Given list of floating point numbers. Convert every number into string and then join all the numbers such 
# that they are separated by pipe(|)

list_1=[1,-9.1,5.2,9.8,3,0,-7.5,3.56]
res = map(str, list_1)
print(res)

str1=""
for i in res:
    str1="|".join(res)    
print(str1)
