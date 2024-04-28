# 7. Write a Python program to find the first appearance of the substrings 'not'
# and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with
# 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

str1="The lyrics is not that poor poor!"

def first_appearance(s: str):
   not_pos = s.find("not",0,len(s))
   poor_pos = s.find("poor",0,len(s))
   if not_pos < poor_pos:
      output_string = s.replace(s[not_pos:poor_pos+4], "good")
      print(output_string)
   return (not_pos,poor_pos,output_string)

result=first_appearance(str1)
print(result[0], result[1])
print(result[2])
