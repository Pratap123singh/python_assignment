# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

l1=["abdcc", "aslkcas", "csa"]
dict1=dict()
l2=list()

def longest_word(l: list):
    for idx in range(0,len(l),1):
        dict1[l[idx]] = len(l[idx])

    for k,v in dict1.items():
        if v == max(dict1.values()):
            word = k
    
    return (word,max(dict1.values()))

result= longest_word(l1)
print(f"The longest word is: {result[0]}")
print(f"The length of longest word is: {result[1]}")
