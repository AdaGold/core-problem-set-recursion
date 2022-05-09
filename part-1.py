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
    else:
        return n * factorial(n-1)


# reverse
def reverse(word):
    if len(word) == 0:
        return ""

    return word[len(word)-1]+ reverse(word.rstrip(word[len(word)-1]))


# bunny
def bunny(n):
    if n == 0:
        return 0
    return bunny(n-1) + 2


# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    
    if parens[0] == "(" and parens[-1] == ")":
        return is_nested_parens(parens[1:-1])
    else:
        return False
