# 6. Find all occurrences of “USA” from right to left in a given string ignoring the case. also display the
# starting position
# Given:
# str1 = "Welcome to USA. usa awesome, isn't it?
# Expected answer : 16, 11

str1 = "Welcome to USA. usa awesome, isn't it? USA USA USA usa"
sub = "usa"
lower_str = str1.lower()
print(str1)
print(lower_str)
def count_substring(str1:str, sub:str):
    count=0
    start=0
    end=len(str1)
    while start<len(str1):
        position = str1.find(sub,start,end)

        if position != -1:
            start = position + 1
            count+=1
        else:
            break
    return count

print(count_substring(lower_str,sub))