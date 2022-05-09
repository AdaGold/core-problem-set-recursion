# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0: 
        raise ValueError
    
    if n == 1 or n == 0: #ok I know (now) this can be just n == 0
        #but I feel bad about changing my original solution
        #after reading the explanation
        return 1
    
    return factorial(n-1) * n



# reverse
def reverse(string):
    if len(string) <= 1:
        return string

    return "".join([string[-1], reverse(string[1:-1:]), string[0]])


# bunny
def bunny(count):
    if count == 0:
        return 0
    return bunny(count - 1) + 2


# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True
    elif parens == "(" or parens == ")":
        return False
    return parens[0] == "(" \
            and parens[-1] == ")" \
            and is_nested_parens(parens[1:-1:])
    ## In hindsight the first two lines of this return
    # could be inside the function instead of in the
    # return and it would be more clean

    # I don't understand the what the challenge problem
    # is asking for. What counts as a "new string"?
