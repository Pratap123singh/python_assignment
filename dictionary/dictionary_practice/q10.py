#10. Write a Python program to sum all the items in a dictionary.

d1={1:10, 2:20, 3:30}
sum=0
for e in d1.items():
    print(e[1])
    sum+=e[1]
print("sum of all items in a dictionary: ", sum)

