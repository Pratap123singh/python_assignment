# 45. Write a Python program to verify that all values in a dictionary are the same.
# Original Dictionary:
# {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False

d={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
def same_value(d: dict,x: int):
    d1={k:v for k,v in d.items() if v == x}
    if len(d1) == len(d):
        return True
    else:
        return False

print("For 12: ", same_value(d,12))
print("For 10: ", same_value(d,10))