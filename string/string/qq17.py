# 17. Write a Python function to get a string made of 4 copies of the last two characters
# of a specified string (length must be at least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses

def insert_end(s: str):
    #last_two_char=s[len(s)-2:len(s):1]
    last_two_char=s[-1:-3:-1]
    reverse_last_two_char=last_two_char[::-1]
    result = reverse_last_two_char * 4
    print(result)

insert_end("Python")
insert_end("Exercise")
