# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num < 0:
        raise ValueError 
    if num == 0:
        return 1 
    
    return factorial(num-1) * num 


# reverse
def reverse(string): 
    if not string:
        return ""
    if len(string) == 1:
        return string
    
    return reverse(string[1:]) + string[0]


# bunny
def bunny(count):
    if not count:
        return 0 
        
    return bunny(count-1) + 2
    


# is_nested_parens
def is_nested_parens(parens): 
    stack = []
    return is_nested_parens_helper(parens, stack)
    

def is_nested_parens_helper(parens, stack): 
    if not parens:
        if not stack:
            return True 
        return False 
    
    if parens[0] == ")":
        if not stack:
            return False 
        stack.pop()
    else:
        stack.append("(")
    
    return is_nested_parens_helper(parens[1:], stack) 
        

