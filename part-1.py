# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    if n == 0:
        return 1
    return n * factorial(n -1)


# reverse
def reverse(s):
    if len(s) <= 1:
        return s       
    else:
        return s[-1] + reverse(s[:-1])


# bunny
def bunny(count):
    if count == 0:
        return 0
    elif count == 1:
        return 2
    else:
        return 2 + bunny(count - 1)


# is_nested_parens
def is_nested_parens(parens):
    if parens == "()" or parens == "":
        return True
    elif len(parens) <= 2:
        return False
    else:
        new_string = parens[1:-1]
        return is_nested_parens(new_string)

