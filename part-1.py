# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.
##############################################
# factorial
##############################################
def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError(f"{n} must be a positive integer")
        
    return n*factorial(n-1)


##############################################
# reverse
##############################################
def reverse(text):
    # checks to make sure the length of text is not 
    if len(text) == 0:
        return text
    # adds the first to the end by using string operation
    # text[0] is in a holding area until the recursion is completed
    # reverse then slices the text string starting from the value 1
    return reverse(text[1:]) + text[0]
    

##############################################
# bunny
##############################################
def bunny(count):
    if count == 0:
        return 0
    return bunny(count-1)+2


##############################################
# is_nested_parens
##############################################
# function checks if the length of the string is even first
def is_nested_parens(parens):
    if len(parens)%2 != 0:
        return False
    else:
        # function that will do recursion
        return check_string(parens)

# helper function that has a recursive that returns the string
# without the first and last character
def check_string(parens):
    # condition to break recursion
    if len(parens) == 0:
        return True
    # recursion act 
    elif len(parens) > 0:
        # first and last parenthesis should never be the same
        if parens[0] == parens[-1]:
            return False
        # recursion that removes the first and last character
        return check_string(parens[1:-1])
    else:
        return False

