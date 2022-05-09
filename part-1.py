# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    elif n == 0:
        return 1

    return factorial(n-1) * n


# reverse
def reverse(text):
    if len(text) == 0:
        return text
    return reverse(text[1:]) + text[:1]


# bunny
def bunny(count):
    if count == 0:
        return 0
    ears = 2
    return bunny(count-1) + ears


# is_nested_parens
def is_nested_parens(parens): 
    if parens == "": 
        return True
    elif parens[0] != "(" or parens[-1] != ")":
        return False

    return is_nested_parens(parens[1:-1])

