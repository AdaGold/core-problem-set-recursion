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
    return factorial(n - 1) * n


# reverse
def reverse(text):
    if len(text) == 0:
        return text
    if len(text) == 1:
        return text
    
    return text[-1] + reverse(text[:len(text)-1])


# bunny
def bunny(count):
    if not count:
        return 0
        
    return 2 + bunny(count - 1)


# is_nested_parens
def is_nested_parens(parens):
    if not parens:
        return True
    
    first = parens[0]
    last = parens[-1]

    if first != '(' or last != ')':
        return False
    
    return is_nested_parens(parens[1:-1]) 

