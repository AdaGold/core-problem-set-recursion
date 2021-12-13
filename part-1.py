# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError("N cannot te negative")
    elif n == 0:
        return 1
    
    else:
        return n * factorial(n-1)


# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    else:
        return text[-1] + reverse(text[1:-1]) + text[0]


# bunny
def bunny(count):
    if count == 0:
        return 0
    else:
        return bunny(count - 1) + 2


# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True
    if parens[0] == "(" and parens[-1] == ")":
        return is_nested_parens(parens[1:-1])
    else:
        return False

