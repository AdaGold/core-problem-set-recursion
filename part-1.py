# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    while n >= 0:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    raise ValueError


# reverse
def reverse(text):
    if len(text) == 0:
        return text
    else:
        return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    if count == 0:
        return 0
    else: 
        return 2 + bunny (count-1)


# is_nested_parens
def is_nested_parens(parens):
    if not parens:
        return True
    elif parens[0] != "(" or parens[len(parens)-1] != ")":
        return False 
    else:
        return is_nested_parens(parens[1:-1])

