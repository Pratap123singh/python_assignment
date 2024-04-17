def palindrome(s: str):
    original_s = s
    reverse_s = s[::-1]
    #print(original_s, reverse_s)
    if original_s == reverse_s:
        return 1
    else:
        return 0
    
print(palindrome("abcba"))


