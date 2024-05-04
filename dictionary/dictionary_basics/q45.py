# 45. Write a Python program to verify that all values in a dictionary are the same.
# Original Dictionary:
# {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False

d={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
d1={'Cierra Vega': 12, 'Alden Cantrell': -12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
def verify_values(d: dict):
    r={v for v in d.values()}
    if len(r) == 1:
        return True
    else:
        return False

print(verify_values(d))
print(verify_values(d1))
