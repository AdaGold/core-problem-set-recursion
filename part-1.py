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
        
    return n * factorial(n-1)


# reverse
def reverse(text):
    arr = []
    
    if len(text) == 0:
        return ""
        
    arr.append(text[-1])
    
    text = text[:-1]
    
    # Ultimately return a string
    return ''.join(arr) + reverse(text)
    
        


# bunny
def bunny(count):
    if count == 0:
        return 0
        
    return 2 + bunny(count - 1)


# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True
        
    if parens[0] == "(" and parens[-1] == ")":
        result = 1
    else:
        result = 0
        
    return bool(result * is_nested_parens(parens[1:-1]))


