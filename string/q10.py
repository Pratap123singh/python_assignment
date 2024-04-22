# 10. Count occurrence of spaces, and special characters in given string
# Ex.
# Input: Fgh^f #89
# Expected output :
# Spaces: 1
# Special characters: 2
# Isalnum()

input = "Fg h^f #89@!"
special_char_list="[@_!#$%^&*()<>?}{~:]"


def count_space(s: str):
    spaces = s.count(" ")
    return spaces

def count_special_characters(s: str):
    count_special_characters=0
    for e in special_char_list:
            special_characters = s.count(e) 
            if special_characters == 1:
                 count_special_characters+=1
    return count_special_characters

print("spaces: ", count_space(input))
print("special_characters: ", count_special_characters(input))