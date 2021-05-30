# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    elif n == 0:
        return 1

    return factorial(n-1) * n

# reverse
def reverse(text):
    if len(text) == 0 or len(text) == 1:
        return text
    
    return text[-1] + reverse(text[:-1])
    

# bunny
def bunny(count):
    if count == 0:
        return 0
    
    return 2 + bunny(count-1)
    

# is_nested_parens

def is_nested_parens(parens, left_index=0):
    right_index = len(parens) - 1- left_index

    if not parens or left_index > right_index:
        return True
            
    elif parens[left_index] == "(" and parens[right_index] == ")":
        return is_nested_parens(parens, left_index+1)
        
    else:
        return False
        
