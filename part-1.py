# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n == 0:
        return 1
    if n < 0 :
        raise ValueError
    return n * factorial(n-1)


# reverse
def reverse(text):
    if len(text) == 0:
        return text
    return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    if count == 0:
        return 0
    return bunny(count -1) + 2


# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True
    inner_parens = parens.find("()")
    if inner_parens != -1:
        new_parens = parens[:inner_parens] + parens[inner_parens+2:]
        return is_nested_parens(new_parens)
    else:
        return False
    

