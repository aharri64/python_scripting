# Palindrome Function

'''
Input: A string
Output: Boolean
Purpose: Is the input string a palindrome?
'''


def is_palindrome(ss):
    # base case
    if len(ss) < 2:
        return True

    if ss[0] != ss[-1]:
        return False
    # recrsive case
    return is_palindrome(ss[1:-1])


# print(is_palindrome("hannah"))
x = 'racecar'
print(x[1:-1])
