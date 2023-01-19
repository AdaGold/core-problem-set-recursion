# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    # handle invalid n
    if n < 0:
        raise ValueError
    # base case
    if n == 0:
        return 1
    # recursive case
    return n * factorial(n-1)


# reverse
def reverse(text):
    # handle empty string & single character string
    if len(text) <= 1:
        return text
    # recursive case
    return text[-1] + reverse(text[:-1])


# bunny
def bunny(count):
    # base case
    if count == 0:
        return 0
    # recursive case
    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens):
    # base cases
    if len(parens) == 0:
        return True
    if len(parens) == 1:
        return False
    # recursive case
    if parens[0] + parens[-1] == "()":
        parens = parens[1:] # remove front (
        parens = parens[:-1] # remove back )
        return is_nested_parens(parens)
