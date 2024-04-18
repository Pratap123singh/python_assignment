# Q Given list of strings, sort all the strings by last character
# of that string. . Use lambda function and normal function both.

list1=["abc", "cdb", "zghd", "mcnjka"]
list1.sort()
print(list1)
list1.sort(reverse=False)
print(list1)
list1.sort(reverse=True)
print(list1)
print(sorted(list1, key=lambda s : s[len(s)-1:len(s):1]))

def last_char(list1: list):
    return list1[-1:-2:-1]

print(sorted(list1, key=last_char))
