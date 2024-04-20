# 22. Write a Python program to remove an empty tuple(s) from a list of tuples.
# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']


l = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d'),[],{}]
print(l)
count=len(l)
while(count>0):
    for e in l:
        if len(e) == 0:
            l.remove(e)
    count-=1
print(l)