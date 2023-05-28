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
    
    
    return n * factorial(n - 1)

# reverse
def reverse(text):
    # base case
    if len(text) <= 1: 
        return text
    
    # recursive case
    length = len(text) - 1 
    
    return text[-1] + reverse(text[0:length])

# bunny
def bunny(count):
    if not count: 
        return count
    
    return 2 + bunny(count - 1)

# is_nested_parens
def is_nested_parens(parens): 
    if not parens:
        return True
    
    if parens[0] == '(' and parens[-1] == ')':
        return is_nested_parens(parens[1:-1])
    else:
        return False

