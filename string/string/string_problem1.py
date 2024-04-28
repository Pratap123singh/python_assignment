str1="1333 This is Ram 471 zzzzz aaaa #####"
d=dict()
print("str1: ", str1)
str_lower=str1.lower()

def remove_space(s: str):
    no_space=s.replace(" ","")
    return no_space

def count_char_digit(s: str):
    for e in s:
        d[e]=s.count(e)
    return d

def count_no_of_occurrence_of_max_value():
    max_value=max(count_of_char_digit.values())
    l=list(count_of_char_digit.values())
    count_max_value=l.count(max_value)
    return (max_value, count_max_value)

favourite_character_list=list()

def favourite_character():
    max_value=max(count_of_char_digit.values())
    for k,v in count_of_char_digit.items():
        if v == max_value:
            favourite_character_list.append(k)
    return favourite_character_list

no_space_str=remove_space(str_lower)
count_of_char_digit=count_char_digit(no_space_str)
print("count_of_char_digit: ", count_of_char_digit)
result=count_no_of_occurrence_of_max_value()
print(result)
print(f"The number of favourite characters are: {result[1]}")
print(f"Favourite characters are: {favourite_character()}")
