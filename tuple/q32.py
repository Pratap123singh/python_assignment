# 32. Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.
# Original list of tuples:
# [(1, 2), (2, 3), (3, 4)]
# Sum of all the elements of each tuple stored inside the said list of tuples:
# [3, 5, 7]
# Original list of tuples:
# [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
# Sum of all the elements of each tuple stored inside the said list of tuples:
# [9, -1, 7, 8]

l=[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
l1=list()
for e in l:
    sum=0
    #print(e)
    for e1 in e:
        #print(e1)
        sum=sum+e1
    l1.append(sum)
print(l1)