# 14. Write a Python program that accepts a comma-separated sequence of words as input and
# prints the distinct words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red

str1="yulia, sophie, any, rose, leslie, drew, berrymore, smith, jousha,"
str2=str()
l=list(str1.split())
l.sort(reverse=False)
for e in l:
    str2 = str2 + e

print(f"\nWords in sorted order:-- {str2.replace(",", " ")}\n")
