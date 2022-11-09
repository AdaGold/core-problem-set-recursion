# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    if n == 0 or n==1:
        return 1
    return n * factorial(n-1)

# reverse
def reverse(s):
    if s=="":
        return s
    return reverse(s[1:])+s[0]



# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2+bunny(count-1)
    
# is_nested_parens
def is_nested_parens(parens):
    if parens == '()' or parens == "":
        return True
    elif parens[:1] != "(" or parens[-1:] != ")":
        return False
    else:
        return is_nested_parens(parens[1:-1])

