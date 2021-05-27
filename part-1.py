# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    elif n == 0:
        return 1
    return factorial(n - 1) * n



# reverse

def reverse(s):
    if s == "":
        return ""
    return reverse(s[1:]) + s[0]

# bunny

def bunny(count):
    if count == 0:
        return 0
    return bunny(count - 1) + 2

# is_nested_parens


def is_nested_parens(str):
    if str == "":
        return True
    elif str[0] == "(" and str[-1:] == ")":
        return is_nested_parens(str[1:-1]) 
    return False