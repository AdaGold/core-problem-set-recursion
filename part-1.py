# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n:int) -> int:
    if n < 0:
        raise ValueError
    elif n == 1 or n == 0:
        return 1 
    
    return factorial(n - 1) * n 


# reverse
def reverse(text:str) -> str:
    if text == "":
        return ""      
    elif len(text) <= 1:
        return text 
    
    return text[-1] + reverse(text[:-1])


# bunny
def bunny(count:int) -> int:
    one_pair_bunny_ears = 2

    if not count:
        return 0
    elif count == 1:
        return 2
    
    return one_pair_bunny_ears + bunny(count - 1) 


# is_nested_parens
def is_nested_parens(parens:str) -> bool: 
    if parens == "": 
        return True
    elif parens[0] != "(" or parens[-1] != ")":
        return False

    return is_nested_parens(parens[1:-1])

