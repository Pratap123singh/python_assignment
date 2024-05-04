# 43. Write a Python program to convert more than one list to a nested dictionary.
# Original strings:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}},
# {'S004': {'Saim Richards': 92}}]

l1 = ['S001', 'S002', 'S003', 'S004']
l2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
l3 = [85, 98, 89, 92]

l=list(zip(l1,l2,l3))
ll = [{x: {y: z}} for x,y,z in l]
#print(type(ll))
print(ll)

