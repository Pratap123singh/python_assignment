# 28. Write a Python program. There is a dictionary where values contain list of integers.
# So, program should sort that list and return complete dictionary
# Ex. 
# i/p
# {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# o/p
# {'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}

d={'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
d1=dict()
def sort1(l: list):
    l.sort(reverse=False)
    return l
for k,v in d.items():
     d1[k]=sort1(v)
print(d1)

