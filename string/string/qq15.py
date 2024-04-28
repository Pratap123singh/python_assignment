# 15. Write a Python function to create an HTML string with tags around the word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

def add_tags(tag: str, s: str):
    s1= f"<{tag}>" + s + f"<{tag}>"
    return s1
print(add_tags("i","python"))
print(add_tags("b","python"))
