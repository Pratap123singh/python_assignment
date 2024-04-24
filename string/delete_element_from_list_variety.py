l=[1,2,3,4,5,[56,57]]
l1=l.copy()
# for e in l:
#     print("e: ", e)
#     del e
# print(l)
# print(l1)

for idx in range(0,len(l),1):
    print(f"len(l): {len(l)}, l[{idx}]: {l[idx]}")
    if l[idx] == 4:
        del l[idx]
        print("l: ", l)
        break
    #print("l: ", l)

print("l1: ", l1)