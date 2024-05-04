# 35. Write a Python program to sort dictionary by value.
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

d={'Math':81, 'Physics':83, 'Chemistry':87}

print(dict(sorted(d.items(), key = lambda x:x[1])))
print(dict(sorted(d.items(), key = lambda x:x[1], reverse=True)))