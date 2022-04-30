# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError('n cannot be negative')
    elif n == 0:
        return 1
    return n*factorial(n-1)


# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]



# bunny
def bunny(count):
    if count == 0:
        return count
    return bunny(count-1) + 2


# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    elif parens[0] == "(" and parens[-1] == ")":
        return is_nested_parens(parens[1:-1])
    return False


# challenge: is_nested_parens without creating new strings
def is_nested_parens(parens,start=0,end=-1):
    if len(parens) == 0 or start-1 == len(parens)+end:
        return True
    elif parens[start] == "(" and parens[end] == ")":
        return is_nested_parens(parens,start+1,end-1)
    return False

