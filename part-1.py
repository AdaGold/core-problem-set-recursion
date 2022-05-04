# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    if n == 0:
        return 1

    return n * factorial(n-1)


# reverse
def reverse(text):
    if len(text) == 0:
        return ""

    return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    if count == 0:
        return 0

    return bunny(count-1) + 2


# is_nested_parens
# Solution 1:
def is_nested_parens(parens):
    if parens == "":
        return True
    if parens[0] != "(" or parens[-1] != ")":
        return False
    
    return is_nested_parens(parens[1:-1]) 

# Solution 2:
def is_nested_parens(parens):
    if len(parens) <= 1:
        return True
    if parens[0] == "(" and parens[-1] == ")":
        return is_nested_parens(parens[1:-1])
    else:
        return False

