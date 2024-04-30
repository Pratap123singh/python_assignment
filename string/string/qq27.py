# 27. Write a Python program to remove existing indentation from all of the lines in a given text.
# (do both using library and without library)
import textwrap
para="""
    Nature around us is a gift. We need to handle it wisely.
    Nature's gifts are for everyone and many generations. 
    Every generation, need to think before making a damage to these gifts.
    """
print(textwrap.dedent(para))

print("---------------------------------------------------------------------------------------")
para2=str()
para3=para.split('.')
print(type(para3))
count=0
s1=0
# def _4_space(p: str):
#     count=0
#     for e in p:
#         if e == " ":
#             count+=1
#         if count == 4:
#             p1=p[4::]
#             count=0
#     _4_space(p1)
#     return p1


p1=para[4::]
print(p1) 