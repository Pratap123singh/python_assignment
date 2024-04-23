str1="hello this is pranjal is pratap is is pranjal is pratap is"

#first occurrence of is
print(str1.index("is",0,len(str1)))

#first occurrence of pranjal pratap is

l=["pranjal","pratap","is"]
t=tuple(l)
print(t)
for e in t:
    index=str1.index(e)
    print(f"first occurrence index of {e} is {index}")

#last occurrence of pranjal pratap is

l=["pranjal","pratap","is"]
t=tuple(l)
print(t)
for e in t:
    index=str1.rindex(e)
    print(f"last occurrence index of {e} is {index}")

# Finding nth occurrence from start of substring
occurrence=3
substring="is"
def nth_occurrence(s: str, substring: str):
    i=-1
    for idx in range(0,occurrence,1):
        i=str1.find(substring,i+1,len(s))
    return (i)

print(f"nth_occurrence(str1,substring): {nth_occurrence(str1,substring)}")

# Finding nth occurrence from last of substring
#2nd from last
str2="is is is pranjal"
n=int(input("enter position of occurrence from last: "))
substring="is"
occurrence=str2.count(substring)-(n-1)
print(occurrence)
def nth_occurrence_from_last(s: str, substring: str,o: int):
    i=-1
    for idx in range(0,o,1):
        i=str2.find(substring,i+1,len(s))
    return -(len(s)-i)

print(f"{n} occurrence from last (str1,substring): {nth_occurrence_from_last(str2,substring,occurrence)}")
