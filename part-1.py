# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial

def factorial(n):
    if (n == 0) or (n == 1):
        return 1
    elif n < 0: 
        raise ValueError("n shouldn't be a negative number")
    else: 
       return (n * factorial(n - 1))


# reverse

def reverse(text):
    if text == "":
        return text
    else: 
        return reverse(text[1: ]) + text[0]

# bunny

def bunny(count):
    if count == 0:
        return 0
    else:
        return (2 + bunny(count - 1))

# is_nested_parens

def is_nested_parens(parens):
    if parens == "":
        return True
    elif parens[0] == "(" and parens[-1] == ")":
        return is_nested_parens(parens[1:-1])
    else:
        return False
