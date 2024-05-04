# 43. Write a Python program to convert more than one list to a nested dictionary.
# Original strings:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]

l1=['S001', 'S002', 'S003', 'S004']
l2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
l3=[85, 98, 89, 92]
d1=dict()
d2=dict()

for k in l2:
    for v in l3:
        d1[k]=v
        l3.remove(v)
        break
print("d1: ", d1)

for k in l1:
    for k,v in d1.items():
        t={k:v}
        d2[k]=t

print(d2)