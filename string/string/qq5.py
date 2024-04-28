# 5. Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'
# Sample String : 'Hello', 'World'
# Expected Result : 'Wollo Herld'
# Test cases:
# a. both empty string input b. 'a' , 'abc' c. '' 'abc' d. '123' 'wow'

str1="hello"
str2="world"

str3=str2.replace(str2[0:2:1],str1[0:2:1])
print(str3)

str4=str1.replace(str1[0:2:1],str2[0:2:1])
print(str4)

result = str4 + " " + str3
print(f"result: {result}")