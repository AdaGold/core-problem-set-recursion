# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError
    return n * factorial(n-1)
    


# reverse
def reverse(text):
    if len(text) == 0:
        return text
    return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    # base case
    if count == 0:
        return 0
    
    # code that returns the function calls
    return bunny(count-1) + 2


# is_nested_parens
def is_nested_parens(parens, left_index = 0):
    right_index = len(parens) - 1 - left_index

    if len(parens) == 0:
        return True
    if left_index >= right_index:
        return True
    
    if parens[left_index] == "(" and parens[right_index] == ")":
        return is_nested_parens(parens,left_index+1)
    else: 
        return False