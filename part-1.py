# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError("Number must be positive")
    if n == 0:
        return 1
    
    return factorial(n-1) * n


# reverse
def reverse(text):
    if not text or len(text) == 1:
        return text

    first = text[0]
    last = text[-1]
    return last + reverse(text[1:-1]) + first


# bunny
def bunny(count):
    if not count:
        return 0
    if count == 1:
        return 2
    return bunny(count-1) + 2


# is_nested_parens
def is_nested_parens(parens):
    if not parens:
        return True
    elif parens[0] == ")" or parens[-1] == "(":
        return False
    else:
        is_inner_nested = parens[1:-1]
        return is_nested_parens(is_inner_nested) 
    

