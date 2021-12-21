# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n< 0:
        raise ValueError('No negative numbers')
    if n == 0:
        return 1
    return n * factorial(n-1)


# reverse
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]


# bunny
def bunny(count):
    if count == 0:
        return 0
    else:
        return bunny(count-1) + 2


# is_nested_parens

def is_nested_parens(parens):
    if parens == "":
        return True
    
    if parens[0] == "(" and parens[-1] == ")":
        return is_nested_parens(parens[1:-1])
    else:
        return False
