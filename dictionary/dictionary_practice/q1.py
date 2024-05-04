#1. Write a Python script to sort (ascending and descending) a dictionary by value.
print("\n")
d1={1:"ram", 3:"geeta", 2:"sita"}

print("Ascending: ",dict(sorted(d1.items(), key = lambda x : x[1])))
print("Descending: ", dict(sorted(d1.items(), key = lambda x : x[1],reverse=True)))

