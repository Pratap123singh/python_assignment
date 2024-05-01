from itertools import permutations

x=input("enter a number: ")
odd_number = set()
for i in range(1,len(x)+1,1):
    for j in permutations(x, i):
        current=int("".join(j))
        if current % 2 != 0:
            odd_number.add(current)
print(odd_number)