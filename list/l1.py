l1=[1,2,13,-9,121,33,-25,5,8]
l2=[e for e in l1 if e > 3]
print(l2)

_11 = [e for e in l1 if e % 11 == 0]
print(_11)

l3 = [e if e > 3 else None for e in l1 ]
print(l3)

print("---------------------------insert---------------------------")
l2=[10,20,30,40,50]
print(l2)
l2.insert(3,-50)
print(l2)

print("---------------------------update---------------------------")
l2[3]=-60
print(l2)

print("---------------------------remove---------------------------")
l2.remove(-60)
print(l2)

print("---------------------------slicing---------------------------")
l4=[10,20,30,40,50,60]
print(f"l4[2:4]: {l4[2:4]}")
print(f"l4[-5:-1]: {l4[-5:-1]}")
print(f"l4[3:5:2]: {l4[3:5:2]}")
print(f"l4[0:5:2]: {l4[0:5:2]}")


print("---------------------------shallow copy---------------------------")
l5=[10,20,30,40]
print(l5)
l6=l5[::]   #shallow copy
print(l6)
l5.remove(30)
print(l5)
print(l6)

print("---------------------------shallow copy---------------------------")
l6=[10,[20,30],[40,50]]
l7=l6[::]   #shallow copy
print("l6: ", l6)
print("l7: ", l7)
print("after removing 10")
l6.remove(10)   #list l6 length get changed
print("l6: ", l6)
print("l7: ", l7)
#l6[2][0] = 400 ------- IndexError
l6[1][0] = 400      #modify list element
print("l6: ", l6)
print("l7: ", l7)

print("---------------------------copy by assignment---------------------------")
l8 = [1,2,3,4]
l9 = l8 #copy by assignment
print("l8: ", l8)
print("l9: ", l9)
l8.remove(2)
print("l8: ", l8)
print("l9: ", l9)

print("---------------------------search an element---------------------------")
l10=["a","b","c",1,2]
if "a" in l10:
    print("yes")
else:
    print("no")

print("---------------------------concat---------------------------")
l11=[10,20,-30]
l12=['a','b',30]
l13 = l11 + l12 
print("l13: ", l13)

print("---------------------------multiply---------------------------")
l14=[1,2,'a']
l14 = l14 * 2
print("l14: ", l14)

print("---------------------------access element---------------------------")
print(l14[2])
print(l14.index(2))

# print("---------------------------replace element through slice---------------------------")
# l15=['a',11,'b',10,20,30,40]
# l15[::2]=[500,500]
# print(l15)


print("---------------------------delete element through slice---------------------------")
l15=['a','b',10,[10,'a'],20,30,40]
del l15[2:3:1]
print(l15)

print("---------------------------delete every alternate element through slice---------------------------")
l15=['a','b',10,[10,'a'],20,30,40]
del l15[::2]
print(l15)

print("---------------------------pop---------------------------")
l16=['a','b',10,[10,'a'],20,30,40]
l16.pop()
l16.pop()
l16.pop()
l16.pop()
print(l16)

print("---------------------------reverse---------------------------")
l18=['a','b',10,[10,'a'],20,30,40]
l18.reverse()
print(l18)

print("---------------------------reverse through slice---------------------------")
l18=['a','b',10,[10,'a'],20,30,40]
print("l18[::-1]: ", l18[::-1])
print("l18: ", l18) #original list do not get reversed because shallow copy me reverse ho raha h


print("---------------------------> , <---------------------------")
l19=[10,20,30,40]
l20=[10,20,30,60]
print("l19>l20: ", l19>l20)
print("l19<l20: ", l19<l20)
l20.pop()
print(l20)
print("l19<l20: ", l19<l20)

print("---------------------------unpacking---------------------------")

l21=[10,20,40,-60]
a,*b,c=l21
print(f"a: {a}, b: {b}, c: {c}")