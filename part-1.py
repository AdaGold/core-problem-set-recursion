# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError("n must be greater than 0")
        
    return n * factorial(n -1)


# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    if count <= 0:
        return 0
        
    return 2 + bunny(count -1)


# is_nested_parens
def is_nested_parens(parens):
    print(parens)
    if len(parens) == 0:
        return True
    elif parens[0] == "(" and parens[-1] == ")":
        return is_nested_parens(parens[1:-1])
        
    return False

