# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    while n > -1:
        # defining base case    
        if n == 1 or n == 0:
            return 1
        
        # defining recursive case
        return factorial(n-1) * n
    raise ValueError


# reverse
def reverse(text):
    # define base case
    if len(text) <= 1:
        return text
    # define recursive case
    while len(text) > 1:
        return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens):
    if not parens:
        return True
    if parens[0] == "(" and parens[-1] == ")":
        return is_nested_parens(parens[1:-1])
    else:
        return False

