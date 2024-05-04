# 44. Write a Python program to filter the height and width of students, which are stored in a dictionary.
# Original Dictionary:
# {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}

d={'Cierra Vega': (6.2, 75), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}

for k,v in d.items():
    print(v[0],v[1])

r={k:v for k,v in d.items() if v[0] > 6 and v[1] > 70}
print(r)
