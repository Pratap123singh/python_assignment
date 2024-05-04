# 34. Write a Python program to count the total number of items under all keys in a dictionary value that is a list.
# Ex. 
# i/p {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# o/p total values : 5

d={'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
count=0
for k,v in d.items():
    for e in v:
        count+=1
print(count)
