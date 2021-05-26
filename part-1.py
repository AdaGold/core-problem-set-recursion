# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):

    if num < 0:
        raise ValueError
    
    if num == 0:
        return 1
    
    return num * factorial(num - 1)


# reverse
def reverse(string):

    if len(string) == 0:
        return string
    
    return string[-1] + reverse(string[:-1])


# bunny
def bunny(count):
    
    if count == 0:
        return 0
    return 2 + bunny(count - 1)


# is_nested_parens
def is_nested_parens(parens):
    
    if len(parens) < 1:
        return True
    
    elif parens[0] != "(" or parens[-1] != ")":
        return False
    
    else:
        return is_nested_parens(parens[1:-1])

