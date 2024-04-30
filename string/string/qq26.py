# 26. Write a Python program to display formatted text (width=50) as output.
# a. using library (hint. textwrap)
# b. without using any library
# Sample input
# para = """Nature around us is a gift. We need to handle it wisely.
# Nature's gifts are for everyone and many generations. Every generation,
# need to think before making a damage to these gifts."""

# width=50

# output:(-> and <- arrow are shown to highlight start and end of line)
# ->Nature around us is a gift. We need to handle it <-
# ->wisely.Nature's gifts are for everyone and many g<-
# ->enerations. Every generation,need to think before<-
# -> making a damage to these gifts.

para = """Nature around us is a gift. We need to handle it wisely.Nature's gifts are for everyone and many generations. Every generation, need to think before making a damage to these gifts."""

def func1(s: str):
    str1=str()
    for e in s:
        str1=str1+e
        if len(str1) == 50:
            print(f"{"->"} {str1} {"<-"}")
            str1=""
    else:
        print(f"{"->"} {str1}")

func1(para)
