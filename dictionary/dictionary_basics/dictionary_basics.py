from math import sqrt
#creation
d={'k1':1,'k2':2,'k3':3,'k4':4}
d1=dict([('k1',10),('k2',20),('k3',30)])
print(d)
print(d1)

#assigning
d1['k1']=101        #-----d1 get modified
print(d1)           #modified d1 is printed

#extracting
print(d1['k1'])
print(d1['k2'])

#delete
del d1['k2']
print(d1)

#display all key value pairs
for k,v in d1.items():
    print(k,":",v, d1[k])

#display all keys
for k in d1.keys():
    print(k)

#display all values
for v in d1.values():
    print("vlaues: ",v)

#if all keys are numeric sort all keys 
d3={1:89, 5:90, 2:91, 30:85, 20:89, 11:95}
print(sorted(d3))

#sort the dictionary keys using lambda
print(f"sort keys ascending order: {dict(sorted(d3.items(), key = lambda x : x[0], reverse=False))}")
print(f"sort keys decending order: {dict(sorted(d3.items(), key = lambda x : x[0], reverse=True))}")

#sort the dictionary Values using lambda
print(f"sort values ascending order: {dict(sorted(d3.items(), key = lambda x : x[1], reverse=True))}")
print(f"sort values descending order: {dict(sorted(d3.items(), key = lambda x : x[1], reverse=False))}")

#To form a dictionary from two list
l1=['a','b',15]
l2=[10,20,'c']
print(dict(zip(l1,l2)))
print(dict(zip(l2,l1)))

#To print dictionary
f=dict({'one': 1, 'three': 3}, two=2)
print(f)

#To pop an key from dictionary
d4=dict([('k1',10),('k2',20),('k3',30)])
print("d4: ", d4)
v=d4.pop('k2')
print(d4)
print("v: ", v)

print("-----------------------------------------------------------------------------------")
#To pop a values from dictionary
d4=dict([('k1',10),('k2',20),('k3',30)])
d5=dict([('k1',10),('k2',20),('k3',30)])
for k,v in d4.items():
    v=d5.popitem()
    print("v: ", v)

print("-----------------------------------------------------------------------------------")
#Copy
d6=dict([('k1',100),('k2',20),('k3',30)])
d7=d6.copy()
print("d6: ", d6)
print("d7: ", d7)
print("id(d6): ", id(d6))
print("id(d7): ", id(d7))

print("-----------------------------------------------------------------------------------")
#get
d8=dict([('k1',100),('k2',20),('k3',30)])
print("d8.get('k2'): ", d8.get('k2'))

print("-----------------------------------------------------------------------------------")
#reversed
d8=dict([('k1',100),('k2',20),('k3',30)])
print(reversed(d8))         #----> object returned hoga
print(list(reversed(d8)))
print(list(reversed(d8.keys())))

print("-----------------------------------------------------------------------------------")
#assign
d9={'k21':1, 'k2':2}
d9['k21'] = 45
print(d9)
d9['this key k3 does not exist in d9, therefore a key is created'] = 56
print(d9)

#iter(d)
print("-----------------------------------------------------------------------------------")
print(list(iter(d9.keys())))
print(list(iter(d9.values())))
print(list(iter(d9.items())))

print("-----------------------------------------------------------------------------------")
#max, min
print(max(d9))
print(min(d9))
print(max(d9.keys()))
print(min(d9.keys()))
print(max(d9.values()))
print(min(d9.values()))
print(max(d9.items()))
print(min(d9.items()))

print("-----------------------------------------------------------------------------------")
#d.update() ---- update values of a key
d11={'k1': 10, 'k2': 20, 'k3': 45}
d11.update(k1=41, k2=89)
print(d11)
print("-----------------------------------------------------------------------------------")

#concatenate two or more dictionaries ----> pipe symbol
d12={'k1':73}
d13={'k2': 78, 'k3': 56}
d14={'k1': 9999, 'k7': 48}
print(d12|d13|d14)

print("-----------------------------------------------------------------------------------")
#dictionary comprehension
d15 = {x: x**2 for x in range(1,10)}
print(d15)
d16 = {y: sqrt(y) for y in range(1,10)}
print(d16)
d_odd = {k:v for k,v in d15.items() if v%2 != 0}
print(d_odd)
d_even = {k:v for k,v in d15.items() if v%2 == 0}
print(d_even)

print("**************************************************************************")
#dictionary packing and unpacking + concatenation
d17={'one':1, 'two':2, 'three':3}
d18={'four':4, 'five':5, 'six':6}
combination={**d17, **d18}
print(combination)
print(d17|d18)

print("**************************************************************************")
#how to create a dictionary from two list
d23=dict()
_keys=['k1','k2','k3']
_values=[10,20,30]
for k in _keys:
    for v in _values:
        d23[k] = v
        _values.remove(v)
        break
print("create a dictionary from two list: ",d23)

print("**************************************************************************")

#creation of a dictionary
d24=dict({'one': 1, 'three': 3}, two=2)
print(d24)

#map function
d25=dict({'k1':25, 'k2':36}, two = 49)
print(d25)
r=map(lambda x: x**0.5, d25.values())
print(list(r))

