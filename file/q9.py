# 9. Write a Python program to count the number of lines in a text file.

with open("file.txt", "r") as f:
    l=f.readlines()
    print(l)
count=0
for e in l:
    count+=1
print(f"The number of lines are: {count}")
