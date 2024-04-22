str1= "BANANA"
sub="ANA"

#print(str1.count(sub))

def count_substring(str1: str, sub: str):
    count=0
    start=0
    end=len(str1)
    while start < len(str1):
        pos = str1.find(sub,start,end)
        print(f"pos: {pos}")
        print(f"start: {start}")
        if pos != -1:
            start=pos+1
            count+=1
        else:
            break
    return count

print(count_substring(str1,sub))