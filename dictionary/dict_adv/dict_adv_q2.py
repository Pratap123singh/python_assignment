# 2. Given a dictionary of students and their favourite colours:
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
# a. Find out how many students are in the list
# b. Change Lisa’s favourite colour
# c. Remove 'Jenny' and her favourite colour

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}

def _count_student(d: dict):
    count_student = {k for k in d.keys()}
    #print((count_student))
    return len(count_student)

print(_count_student(people))

def _change_color(d: dict, name:str, color: str):
    d[name] = color
    return d
name=input("Enter name: ")
color=input("Enter new color: ")
print(_change_color(people, name, color))

#to remove jenny
del people['Jenny']
print(people)