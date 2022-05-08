# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    try:
        if num == 0:
            return 1
        return num * factorial(num-1)
    except:
        raise ValueError


# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    if count == 0:
        return 0
    return bunny(count-1) + 2 


# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True
    elif len(parens) <= 2 and parens != "()":
        return False
    return is_nested_parens(parens[1:-1])

