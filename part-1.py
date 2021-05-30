# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num): 
    if num < 0: 
        raise ValueError("Number must be greater than zero")
    elif num <= 1: 
        return 1 
    return num * factorial(num -1)

# reverse
def reverse(text):
    if len(text) <= 1: 
        return text
    return reverse(text[1:]) + text[0]

# bunny
def bunny(count): 
    if count < 1: 
        return 0 
    return 2 + bunny(count -1)

# is_nested_parens
def is_nested_parens(parens): 
    if len(parens) == 0: 
        return True 
    elif parens[0] + parens[-1] == "()":
        return is_nested_parens(parens[1:-1])
    else: 
        return False

