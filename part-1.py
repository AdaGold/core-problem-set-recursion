# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial (n):    
    # check validate input
    if n < 0:
        raise ValueError("n cannot be negative")    
    # Base
    if n <= 1:
        return 1
    # Recursive
    return n * factorial(n - 1)


# reverse
def reverse (text):   
    # Base
    if len(text) == 0:
        return text
    # Recursive (remaining + first)
    return reverse (text[1:]) + text[0]


# bunny
def bunny (count):   
    # Base
    if count == 0:
        return 0 
    # Recursive
    return bunny(count - 1) + 2


# is_nested_parens
def is_nested_parens (parens):  
    # Base
    if len(parens) == 0:
        return True
    elif '()' not in parens:
        return False
    # Recursive
    return is_nested_parens (parens.replace('()', ''))

