# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num): 
    if num < 0:
        raise ValueError
    if num <= 1:
        return 1 
        
    return num * factorial(num - 1)



# reverse
def reverse(string):
    if len(string) == 0: 
        return ""
        
    return string[-1] + reverse(string[:-1])


# bunny
def bunny(num):
    if num ==0:
        return 0

        
    return 2 + bunny(num-1)


# is_nested_parens
def is_nested_parens(parens, left_index = 0):
    
    right_index = len(parens) - 1 - left_index
    
    if len(parens) == 0:
        return True
    
    
    if left_index > right_index:
        return True
        
    if parens[left_index] == "(" and parens[right_index]  == ")":
        return is_nested_parens(parens, left_index + 1)
    else:
        return False

