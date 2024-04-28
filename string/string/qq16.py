# 16. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

def insert_sting_middle(tag: str, s: str):
    s1=str()
    l=list(tag)
    idx = len(l)//2
    l.insert(idx,s)
    for e in l:
        s1  = s1 + e
    return s1
print(insert_sting_middle("{{}}", "PHP"))
print(insert_sting_middle("[[]]", "Python"))
