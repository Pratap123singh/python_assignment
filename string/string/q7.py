# 7. Find all overlapping occurrences of given substring in given string
# Ex.
# String = 0111
# Substring = 11
# Expected answer : 2
# String : ANANAAAANNN
# Substring: ANA
# Expected answer : 2
# String : ANANAAAANNN
# Substring: AA
# Expected answer : 3

str1="0111"
sub1="11"
str2="ANANAAAANNNANA"
sub2="ANA"
str3="ANANAAAANNN"
sub3="AA"

def count_substring(str1:str, sub:str):
    count=0
    start=0
    end=len(str1)
    while start<len(str1):
        position=str1.find(sub,start,end)

        if position != -1:
            start=position+1
            count+=1
        else:
            break
    return count

print(count_substring(str1,sub1))
print(count_substring(str2,sub2))
print(count_substring(str3,sub3))
