l=[{'rec1': {'col1': 1, 'col2': 10, 'col3': 100}},
   {'rec2': {'col1': 2, 'col2':20, 'col3': 200}}, {'rec3': {'col1': 3, 'col2':30, 'col3': 300}}]

l1=list()
l2=list()
l3=list()

for d1 in l:
    for k,v in d1.items():
        for k1,v1 in d1[k].items():
            if k1 == 'col1':
                l1.append(d1[k][k1])
            elif k1 == 'col2':
                l2.append(d1[k][k1])
            elif k1 == 'col3':
                l3.append(d1[k][k1])

def mean_calculation(l: list):
    sum=0
    for e in l:
        sum+=e
    return sum/len(l)

print("the mean of col1 is: ", mean_calculation(l1))
print("the mean of col1 is: ", mean_calculation(l2))
print("the mean of col1 is: ", mean_calculation(l3))