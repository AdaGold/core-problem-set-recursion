# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    # base case
    if n == 0:
        return 1
    if n < 0:
        raise ValueError
    #recursive case
    return n*factorial(n-1)


# reverse
def reverse(text):
    # base case
    if len(text) == 0:
        return ""
    elif len(text) == 1:
        return text
    # recursive case
    return reverse(text[1:])+text[0]


# bunny
def bunny(count):
    # base case
    if count == 0:
        return 0 
    # validate
    if count < 0 or count != int(count):
        raise ValueError
    # recursive case
    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens): 
    #base case
    if len(parens) == 0: 
        return True
    elif parens[0] != "(" or parens[-1] != ")":
        return False
    #recursive case
    return is_nested_parens(parens[1:-1])

