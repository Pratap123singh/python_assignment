#19. Write a Python program to combine two dictionary by adding values for common keys.
d1={1:10, -2:20, 3:30, -4:40, 5:30, 6:30}
d2={-2:10, 3:30, -7:40}
d3={'a': 100, 'b': 200, 'c':300}
d4={'a': 300, 'b': 200, 'd':400}

d3=dict()

for k1,v1 in d1.items():
    sum=0
    for k2,v2 in d2.items():
        if k1 == k2:
            sum=v1+v2
            d3[k1] = sum
print(d3)
