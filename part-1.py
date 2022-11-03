# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial

def factorial(n):
    if n < 0: 
        raise ValueError
        
    else:
        if n == 0:
            return 1

        return factorial(n-1) * n


# reverse

def reverse(text):
    if len(text) < 2:
        return text
        
    else:
        return reverse(text[1:]) + text[0]


# bunny

def bunny(count):
    if count == 0:
        return 0
        
    else:
        return bunny(count-1) + 2


# is_nested_parens

def is_nested_parens(parens):
    if len(parens) == 0 or parens == '()':
        return True
    
    else:
        if parens[0] == ')' or parens[-1] == '(':
            return False
    
    return is_nested_parens(parens[1:-1])