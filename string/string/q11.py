# 11. Given a paragraph count number of words, sentences. Every sentence ends with either . or ? or !
# Print Count of how many normal sentences ending with . , how many interrogative sentences ( ending
# with ?) and how many exclamatory sentences ( ending with !).
# Ex.
# Input : “I am at CDAC. What about you? I am surprised by current weather!”
# Normal sentence : 1
# Interrogative: 1
# Exclamatory : 1

input= "I am at CDAC. What about you? I am surprised by current weather! hello this me. hi?"

def count_words(s: str):
    count=0
    l1=s.split(" ")
    for e in l1:
        count+=1
    return count

def count_sentence(s: str):
    count_normal=0
    count_interrogative=0
    count_exclamatory=0
    for idx in range(0,len(s),1):
        if s[idx] in ["."]:
            count_normal+=1
        elif s[idx] in ["!"]:
            count_interrogative+=1
        elif s[idx] in ["?"]:
            count_exclamatory+=1
    return (count_normal, count_interrogative, count_exclamatory)

print(f"The number of words in the sentence: {count_words(input)}")
sentence_type=count_sentence(input)
print(f"Normal sentence: {sentence_type[0]}")
print(f"Interrogative sentence: {sentence_type[1]}")
print(f"Exclamatory sentence: {sentence_type[2]}")