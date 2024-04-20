#24. Write a Python program to count the elements in a list until an element is a tuple.

l=[1,2,3,(10,20),10]
count=0
for e in l:
    #print(type(e))
    if type(e) == int:
        count+=1
    if type(e) == tuple:
        break
print(count)