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
    return n * factorial(n - 1)


# reverse
def reverse(text):
    if len(text) == 0:
        return text
    if len(text) > 0:
        return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    if count == 0:
        return count
    if count > 0:
        return bunny(count - 1) + 2


# is_nested_parens
def is_nested_parens(parens): 
    if len(parens) == 0:
        return True
    
    inner_case = parens[1:-1]
    outer_case = parens[0] == "(" and parens[-1] == ")"
    
    return outer_case and is_nested_parens(inner_case)

