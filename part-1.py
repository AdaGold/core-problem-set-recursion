# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

#=============================================================================
# factorial

def factorial(n):
    if n == 0:
        return 1
    try:
        return factorial(n-1) * n 
    except RecursionError:
        raise ValueError

#=============================================================================
# reverse

def reverse(text):
    if len(text) == 0:
        return text
    else:
        # text[1:] slices the string except for the first character 
        return reverse(text[1:]) + text[0]
    
#=============================================================================
# bunny

def bunny(count):
    if count == 0:
        return 0
    else:
        return 2 + bunny (count - 1)

#=============================================================================
# is_nested_parens

def is_nested_parens(parens, i=0, j=0):
    if i == len(parens):
        return j == 0
    
    if parens[i] == "(":
        return is_nested_parens(parens, i+1, j+1)
    elif parens[i] == ")":
        return is_nested_parens(parens, i+1, j-1)
