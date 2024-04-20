
t1=(10,20,30)
empty_t=()
ele=int(input("enter an element to be removed: "))
print(type(set(t1)))
for e in set(t1):
    if e!=ele:
        print(e)
        empty_t=empty_t+(e,)

#print(type(empty_t))
print(empty_t)

"""
t2=(10,20,(200,"hi"),["hello", 210],20,(200,"hi"))
empty_t=()
ele=int(input("enter an element to be removed: "))
print(type(set(t2)))
for e in set(t2):
    for a in set(e):
        if e!=ele:
            print(e)
            empty_t=empty_t+(e,)

#print(type(empty_t))
print(empty_t)
"""