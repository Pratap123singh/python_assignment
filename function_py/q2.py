
def func(l1:list):
    l3=[]
    for idx in range(0,len(l1),1):
        if l1[idx]%11==0:
            l3.append(l1[idx])
    print(l3)
func([10,11,20,121,33])

"""
def divby11(l1:list):
    for e in l1:
        if e%11==0:
            print(e)
divby11([10,20,11,102,22,33])
"""