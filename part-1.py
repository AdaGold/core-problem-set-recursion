# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        raise ValueError
    return n * factorial(n-1)
    


# reverse

def reverse(text):
    if text == "":
        return ""
    if len(text) == 1:
        return text
    return reverse(text[1:]) + text[:1]

# bunny

def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count - 1)

# is_nested_parens

def is_nested_parens(parens):
    if parens == "":
        return True
    else:
        if parens[0] == "(" and parens[-1] == ")":
            parens = is_nested_parens(parens[1:-1])
            return parens
        else: 
            return False
