# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num < 0:
        raise ValueError
    elif num < 2:
        return 1
    
    return factorial(num - 1) * num 


# reverse
def reverse(text):
    if len(text) < 2:
        return text
    
    return text[-1] + reverse(text[1:-1]) + text[0]


# bunny
def bunny(num):
    if num == 0:
        return 0
    
    return bunny(num - 1) + 2


# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True
    if len(parens) == 1:
        return False

    if parens[0] == "(" and parens[-1] == ")":  
        return is_nested_parens(parens[1:-1])
    return False
        

