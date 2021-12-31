# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial

def factorial(n):
    if n < 0:
        raise ValueError ("keep it positive")
    if n == 0:
        return 1
    else: 
        return factorial(n-1) * n



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
    elif count ==1:
        return 2
    else:
        return 2 + bunny(count-1)

# is_nested_parens

def is_nested_parens(parens):
    if parens == "":
        return True
    if parens[0] == "(" and parens[-1] == ")":
        return is_nested_parens(parens[1:-1])
    else:
        return False


