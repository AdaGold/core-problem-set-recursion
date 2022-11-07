# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial

def factorial(n):
    if n < 0:
        raise ValueError
    return 1 if n <= 1 else n * factorial(n - 1)

# reverse

def reverse(text):
    return text[-1] + reverse(text[:-1]) if text else ""

# bunny

def bunny(count):
    return 2 + bunny(count - 1) if count > 0 else 0

# is_nested_parens

def is_nested_parens(string):
    def helper(string, count):
        if not string:
            return False if count else True

        if string[0] == "(":
            return helper(string[1:], count + 1)
        elif string[0] == ")":
            return helper(string[1:], count - 1)

    return helper(string, 0)
