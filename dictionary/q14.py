#14. Write a Python program to sort a given dictionary by key. And output should be a dictionary.

d1={1:10, -2:20, 3:30, -4:40}

print(dict(sorted(d1.items(), key = lambda x : x[0])))
print(dict(sorted(d1.items(), key = lambda x : x[0], reverse=True)))

