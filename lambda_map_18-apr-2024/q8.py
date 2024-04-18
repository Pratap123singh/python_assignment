# Q Given list of integers. Use map function to calculate square of all
# and store in list. Then print sum of all square values.
l1=[1,2,3,4]
def square1(e:int):
    return e*e
s=map(square1,l1)
l2=list(s)
print(f"l2: {l2}")

#print sum of square

def add1(l:list):
    sum1=0
    for idx in range(0,len(l),1):
        sum1=sum1+l[idx]
    return sum1
def add2(l:list):
    sum1=0
    for e in l:
        sum1=sum1+e
    return sum1
print(add1(l2))
print(add2(l2))
