# 25. Write a Python program to create a Caesar encryption.

# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher,
# Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some 
# fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, 
# E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

str0="abcdefghijklmnopqrstuvwyz"
str1="Pranjal"

def ceaser_cipher(s: str):
    s1=str()
    for idx in range(0,len(s),1):
        m=s[idx:idx+1:1]
        i=str0.index(m,0,len(str0))
        n=str0[i-3]
        s1 = s1 + str1[idx:idx+1:1].lower().replace(m,n)
    return s1

print("Original String: ", str1)
print(f"Ceaser Cipher: {ceaser_cipher(str1.lower())}")



