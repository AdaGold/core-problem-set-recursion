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
    else:
        return n * factorial(n - 1)


# reverse
def reverse(text):
    if text == "":
        return ""
    else:
        return text[-1] + reverse(text[:-1])


# bunny
def bunny(count):
    ears = 0
    if count == 0:
        return ears
    else:
        ears = bunny(count - 1) + 2
        return ears


# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True 
    elif parens[0] == "(" and parens[-1] == ")":
        return is_nested_parens(parens[1:-1])
    else:
        return False
        

