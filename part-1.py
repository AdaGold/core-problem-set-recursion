# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial

def factorial(n):
    if n < 0:
        raise ValueError('Number must be greater than zero')
    # base case
    if n == 0:
        return 1
    
    return (n * factorial(n-1))


# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    
    first_letter = text[:1]
    rest_letter = text[1:]
    
    return reverse(rest_letter) + first_letter


# bunny
def bunny(count):
    if count == 0:
        return count 
    
    return bunny(count - 1)  + 2



# is_nested_parens

def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    elif parens[:1] != "(" or parens[-1:] != ")":
        return False
    else:
        return is_nested_parens(parens[1:-1])


