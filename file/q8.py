# 8. Write a python program to find the longest words.

with open("x_file","r") as f:
    s=f.read()
    print(type(s))
    print(s)
    for e in s:
        temp=len(e)
        print(e)
    # r=s.split("\n")
    # print(type(r))
    # z=str(r)
    # print(z)
    # m=z.split(" ")
    # print(max(m))
