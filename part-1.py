# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n<0:
        raise ValueError
    if n == 0:
        return 1
    return n * factorial(n-1)


# reverse
def reverse(text):
    r = len(text)
    if r == 0:
        return text
    return text[r-1] + reverse(text[0:r-1])


# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens):
    
    if parens == "":
        return True
    
    if not parens[0] == "(" or not parens[-1] == ")":
        return False
    
    
    if parens[0] == "(" and parens[-1] == ")":
        return is_nested_parens(parens[1:-1])

