# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial

def factorial(n):
    if n < 0:
        raise ValueError("negative integer")
    if n == 0:
        return 1
    return n*factorial(n-1)

# reverse

def reverse(text):
    if len(text) == 0:
        return text
    else:
         return text[-1] + reverse(text[:-1])

# bunny

def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count -1)

# is_nested_parens

def is_nested_parens(parens):
    if parens == "":
        return True
    elif "()" in parens:
        new_parens = parens.replace("()", "")
        return is_nested_parens(new_parens)
    else:
        return False
