l=[{'rec1': {'col1': 1, 'col2': 10, 'col3': 100, 'col4': 4}},
   {'rec2': {'col1': 2, 'col2':20, 'col3': 200, 'col4': 40}}, {'rec3': {'col1': 3, 'col2':30, 'col3': 300, 'col4': 400}}]

l1=list()
l2=list()
l3=list()
length=0
for d1 in l:
    for k,v in d1.items():
        for k1,v1 in d1[k].items():
            length=len(d1[k])
            l1.append(v1)
print(l1)
#print(length)
sum=0
similar_column_count=0
for i in range(0,length,1):
    for idx in range(i,len(l1),4):
        # print(l1[idx])
        sum+=l1[idx]
        similar_column_count+=1
    mean=sum/similar_column_count
    print("The mean is: ", round(mean,2))
    mean=0
    sum=0