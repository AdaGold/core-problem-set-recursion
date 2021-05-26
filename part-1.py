# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num == 0:
        return 1
    if num <0:
        raise ValueError

    return num * factorial(num - 1)


# reverse
def reverse(s):
    if len(s)==0:
        return s
        
    return reverse(s[1:]) + s[0]


# bunny
def bunny(n):
    if n == 0:
        return 0

    return bunny(n-1) + 2


# is_nested_parens
def is_nested_parens(s):
    open_s = "("
    close_s = ")"
    if len(s)<1:
        return True
    elif s[0]!=open_s or s[-1]!=close_s:
        return False

    return is_nested_parens(s[1:-1])


