
# 3. Sort and print students and their favourite colours alphabetically by name

d = {'Yulia': 'Blue', 'James': 'Red', 'Paras': 'Blue', 'Rohan': 'Black', 'Rekha': 'Green'}
print("\n")
print(dict(sorted(d.items(), key = lambda x : x[0], reverse=False)))
print("\n")
print(dict(sorted(d.items(), key = lambda x : x[0], reverse=True)))
print("\n")
print(dict(sorted(d.items(), key = lambda x : x[1], reverse=False)))
print("\n")
print(dict(sorted(d.items(), key = lambda x : x[1], reverse=True)))
print("\n")