vowel="AEIOU"
str1="banana"
count_kevin=0
count_stuart=0
for idx in range(len(str1)):    
    if str1[idx] in vowel.lower():
        count_kevin+=len(str1)-idx
    else:
        count_stuart+=len(str1)-idx
if count_kevin > count_stuart:
    print("Kevin wins")
elif count_kevin < count_stuart:
    print("Stuart wins")
else:
    print("Draw")




