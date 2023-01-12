# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num == 0:
        return 1
    if num < 0:
        raise ValueError("Number is negative")
    return num * factorial(num-1)


# reverse
def reverse(txt):
    if not txt:
        return txt
    return reverse(txt[1:]) + txt[0]


# bunny
def bunny(count):
    if count == 0:
        return 0
    
    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    if parens[0] == "(" and parens[-1] == ")":
        return is_nested_parens(parens[1:-1])
    else:
        return False

