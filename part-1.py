# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num): 
    if 0 <= num <= 1: 
        return 1 

    elif num < 0: 
        raise ValueError

    return num * factorial(num-1)  


# reverse
def reverse(text): 
    # Base Case 
    if len(text) <= 1:
        return text

    return text[-1] + reverse(text[:-1])


# bunny
def bunny(count): 
    # Base Case
    if count == 1: 
        return 2

    if count == 0: 
        return 0

    return 2 + bunny(count - 1)


# is_nested_parens
def is_nested_parens(parens, left_index = 0): 
    right_index = len(parens) - 1 - left_index
    # Base Case
    if len(parens) == 0: 
        return True 
    
    if left_index >= right_index: 
        return True 
    
    if parens[left_index] == "(" and parens[right_index] == ")":
        return is_nested_parens(parens, left_index + 1)
    else: 
        return False

