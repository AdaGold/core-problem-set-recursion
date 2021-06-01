# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    ''' 
    accepts an integer, n, as a parameter and returns the value of n factorial, aka n!
    '''
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError
    else:
        return n * factorial(n-1)


# reverse
def reverse(text):
    ''' 
    accepts a string as a parameter and returns the reverse of that string 
    '''
    if text == "":
        return text
    elif len(text) < 2:
        return text
    else:
        return reverse(text[1:]) + text[0]



# bunny
def bunny(num):
    '''
    accepts an integer that represents a bunny. each bunny has 2 ears.
    Computes the total number of ears accross all the bunnies recursively.
    '''
    
    if num == 0:
        return 0
    
    return 2 + bunny(num -1)


# is_nested_parens
def is_nested_parens(parens):
    '''
    accepts a string parens of only parentheses. 
    Returns True if those parentheses are properly nested, 
    and False if they are not. 
    '''

    if len(parens) % 2 != 0:                # Base Case #1: if len(parens) is odd number - False
        return False
        
    paren_list = []                         # Make parens a list
    for paren in parens:                    # Use for loop with append() to convert the string into a list
        paren_list.append(paren)
        
    return pop_mid_match(paren_list)
    
def pop_mid_match(paren_list):              # Helper Function
    if len(paren_list) == 0:                # Base Case #2
        return True
        
    mid = len(paren_list) // 2              # Set index [mid] to the middle item

    if paren_list[mid] == ")" and paren_list[mid-1] == "(":
        paren_list.pop(mid)
        paren_list.pop(mid-1)
        return pop_mid_match(paren_list)    # Recursive Solution
    else:
        return False

