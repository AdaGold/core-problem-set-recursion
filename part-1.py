# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):

    if (num == 1 or num == 0):
        return 1
        
    if num < 0:
        raise ValueError
    
    else:
        return num * factorial(num - 1)


# reverse
def reverse(string):
    str = ""
    for element in string:
        str = element + str
    return str    


# bunny
def bunny(count):
    if count == 0:
        return 0
    else:
        return 2 + bunny(count - 1)


# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0: 
        return True
        
    elif parens[:1] != "(" or  parens[-1:] != ")":
        return False
        
    else:
        return is_nested_parens(parens[1:-1])

