# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial

def factorial(n):
    if n == 1: 
        return 1
    elif n == 0: 
        return 1
    elif n < 0:
        raise ValueError
        
    return n * factorial(n - 1)



# reverse
def reverse(text):
    if text == "":
        return ""
    return reverse(text[1:]) + text[0]


# bunny

def bunny(count):
    if not count:
        return count
    else:
        return bunny(count-1) + 2

# is_nested_parens

def is_nested_parens(parens, count = 0):

    if len(parens) == 0:
        return count == 0
    if count < 0:
        return False
    
    if parens[0] == "(":
        return is_nested_parens(parens[1:],count +1)
    elif parens[0] == ")":
        return is_nested_parens(parens[1:], count -1)
        
    
