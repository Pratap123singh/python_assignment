# 8. Given a string in format Emp_name:Emp_id
# If emp_is is perfect square -- > Print only vowels from emp_name
# Else if emp_id is prime -- > print alternate characters from emp_name
# Else if emp_id is odd -- > print sum of ascii values of characters in emp_name
# Else print None

emp_name="pranjalpratapsingh"
emp_id="4"

def check(emp_name: str, emp_id: int):
    vowel=[emp_name.count("a"),emp_name.count("e"),emp_name.count("i"),emp_name.count("o"),emp_name.count("u")]
    print(vowel)
    print(type(vowel))
    for e in ["a","e","i","o","u"]:
        for i in vowel:
            print(f"{e}: {vowel[i]}")
            break


print(check(emp_name,4))