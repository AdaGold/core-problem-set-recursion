# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n<0:
        raise ValueError
    if n <= 1:
        return 1
    return n * factorial(n-1)


# reverse
def reverse(in_str):
    if in_str == "":
        return in_str
    
    first_char = in_str[:1]
    remaining_chars = in_str[1:]
    return reverse(remaining_chars) + first_char


# bunny
def bunny(count):
    if count <= 0:
        return 0
    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True
    elif parens[0] != "(" or parens[-1] != ")":
        return False
    return is_nested_parens(parens[1:-1])

