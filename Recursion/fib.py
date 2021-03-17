'''
input: An integers
Output: An integers
purpose: What is the nth number in the fibonacci sequence?
'''


def fib(n):
    if n < 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(13))
