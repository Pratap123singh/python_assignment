word1 = "abc"
word2 = "pqrw"

def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    c3=""
    if len(word1) >= len(word2):
        length = len(word1)
    else:
        length = len(word2)
        
    for i in range(0,length,1):
        c1=word1[i:i+1:1]
        c2=word2[i:i+1:1]
        c3=c3+c1+c2
    return c3

print(mergeAlternately("abc", "pqr"))