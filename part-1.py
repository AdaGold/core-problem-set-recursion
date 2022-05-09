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
    if text == "":
        return text
    else:
        return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    if count == 0:
        return 0
    
    return 2 + bunny(count - 1)


# is_nested_parens
def is_nested_parens(parens):
    #first base case
    if parens == "":
        return True
    #second base case
    elif parens[:1] == parens[-1:]:
        return False
    else:
        parens = parens[1:-1]
        return is_nested_parens(parens)

