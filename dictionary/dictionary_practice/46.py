# 46. Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}

l1 = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
l2=list()
def dict_sequence(l: list):
    for e in l:
        l2.append(e)
    print(l2)



dict_sequence(l1)