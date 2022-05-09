# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial

def factorial(n):
    """
    The base case is when n is 1, the factorial is 1.
    
    return the product of all the integers so far and n
    """
    if n < 0:
        raise ValueError
    
    if n <= 1:
        return 1
        
    return n * factorial(n-1)  

# reverse

def reverse(text):
    """
    base case: when len(text) == 1 return text
    
    add to the string of previous chars the last char and remove the last char.
    """
    
    if len(text) <= 1:
        return text
    
    return text[-1] + reverse(text[:-1]) 

# bunny

def bunny(count):
    """
    base case: when count == 0 return count
    
    return the total sum and two and decrease the count of bunny by 1
    """
    
    if not count:
        return count
        
    return bunny(count - 1) + 2


# is_nested_parens

def is_nested_parens(parens):
    """
    base case: when len(parens) == 0 return True
    """
    
    if not parens:
        return True
        
    if parens[0] != "(" or parens[-1] != ")":
        return False
    
    return is_nested_parens(parens[1:-1])
