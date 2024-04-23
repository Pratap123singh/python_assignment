# 12. You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w
# Example .
# String : “ABCDEFGHIJKLIMNOQRSTUVWXYZ”
# Width: 4
# Output:
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

str1= "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
#str1= "ABCDEFGHI"
width=int(input("enter width: "))

for idx in range(0,len(str1),width):
    r=str1[idx:idx+width]
    print(r)