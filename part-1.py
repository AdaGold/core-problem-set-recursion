# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n <0:
        raise ValueError
    elif n == 0:
        return 1

    return n * factorial(n-1)


# reverse
def reverse(text):
    if text == "":
        return ""
    
    return reverse(text[1:])+ text[0]



# bunny
def bunny(count):
    if not count:
        return count
    else:
        return 2 + bunny(count-1)



# is_nested_parens
def is_nested_parens(parens):
    open_parens = "("
    close_parens = ")"
    
    if len(parens) == 0:
        return True
    
    elif parens[0]!= open_parens or parens[-1]!= close_parens:
        return False
    
    return is_nested_parens(parens[1:-1])


