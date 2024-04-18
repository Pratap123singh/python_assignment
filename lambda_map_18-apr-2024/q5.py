# Q. Take Employee id and Employee name of 5 employees from user. Store it in dictionary. Print all employees 
# in increasing order of employee Id . Also print all employees in alphabetical order by name.

dict1={1245:"ram",  3253:"gita", 400:"nita", 2451:"sita", 501:"tina"}
#sort them by their id
sorted_key=sorted(dict1.keys())
print(sorted_key)
sorted_dict_key={}
for e in sorted_key:
    sorted_dict_key[e]=dict1[e]
print("All employee in increasing order of their employee id: ")
print(sorted_dict_key)


print("\nAll employee in increasing order of their employee id: ")
print(dict(sorted(dict1.items(), key = lambda x : x[0])))
print("\nAll employee in alphabetical order by name: ")
print(dict(sorted(dict1.items(), key = lambda x : x[1])))