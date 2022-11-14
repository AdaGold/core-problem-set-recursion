# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# These solutions are based on the lecture I took on 11/09/2022
# Tried to understand recursion anyway!

# factorial
def factorial(n):
    
    if n == 0:
        return 1
    if n < 0:
        raise ValueError
        
    return n * factorial(n-1)


# reverse
def reverse(text):

    if text == '':
        return text
    else:
        return reverse(text[1:]) + text[0]


# bunny
def bunny(n):
    
    if n <= 0:
        return 0
        
    return 2 + bunny(n-1)


# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True
    elif parens[0] == parens[-1]:
        return False
    else:
        return is_nested_parens(parens[1:-1])

