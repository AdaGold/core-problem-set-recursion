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
    if not text:
        return text
    else:
        return text[-1] + reverse(text[0:-1])



# bunny
def bunny(count): 
    if count == 0:
        return 0
    else:
        return 2 + bunny(count - 1)


# is_nested_parens
def is_nested_parens(parens):
    if not parens:
        return True
    elif len(parens) % 2 != 0:
        return False
    elif parens[0] == "(" and (parens[-1]) == ")":
        return is_nested_parens(parens[1:-1]) 
    else:
        return False


