# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    
    if n <= 1:
        return 1
    
    return n * factorial(n-1)


# reverse
def reverse(string):
    rev_string = ""
    
    if len(string) == 0:
        return rev_string
    
    rev_string += string[-1]
    string = string[:-1]
    
    return  rev_string + reverse(string)


# bunny
def bunny(count):
    if count == 0:
        return 0
    
    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    if parens[0] == parens[-1]:
        return False
    
    return is_nested_parens(parens[1:-1])
