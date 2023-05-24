# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError("Number must be greater than 0!")

    if not n:
        return 1

    return n * factorial(n - 1)


# reverse
def reverse(s):
    if len(s) <= 1:
        return s

    first_letter = s[0]
    rest = s[1:]

    return reverse(rest) + first_letter


# bunny
def bunny(count):
    if not count:
        return 0

    return bunny(count - 1) + 2


# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True

    return is_nested_parens(parens[1:-1]) and parens[0] == "(" and parens[-1] == ")"

