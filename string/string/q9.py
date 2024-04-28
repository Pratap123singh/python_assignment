# 9. Find all mobile number mentioned in given paragraph of text
# Mobile number is always a 10 digit number no spaces no special characters
# Ex. Input= “this is a good number 9089786756 and 8900000000 is a desired number”
# Expected output: 9089786756 , 8900000000

input = "this is a good number 9089786756 908978#756 and 8900000000 8900000007 is a desired 89000000242 89000 000242 number"

def check_10(num: int):
    t=str(num)
    n=len(t)
    return n
    
m=list()
def find_mobile_number(input: str):
    number=[int(i) for i in input.split() if i.isnumeric()]
    for e in number:
        _10 = check_10(e)
        if _10 == 10:
            m.append(e)
    return m
print(find_mobile_number(input))
