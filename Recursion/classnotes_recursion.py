# Base Case is where it's gonna stop

# Recursion is a way to loop


# sum of all the integers from 0 to n where n is the input
def get_sum(n=0):
    # base case where we don't call our function
    if (n == 0):
        return 0
    # recuresive case we call our function in the return value
    return n + get_sum(n - 1)
    # moving towards our base case


get_sum(0)
get_sum(5)
