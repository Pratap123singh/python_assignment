# 20. Write a Python function to reverse a string if its length is a multiple of 4.

def func1(s: str):
    if len(s)%4 == 0:
        print(s[::-1])
    else:
        print(s)

func1("hell")
func1("hello")
func1("hello ")
func1("hello Paras!")