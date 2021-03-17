# Reverse String Function
# Input: A string
# Output: A string
# Purpose: Reverse a string

def reverse(ss):
    if len(ss) == 0:
        return ""
    return ss[-1] + reverse(ss[:-1])


print(reverse('hello'))
