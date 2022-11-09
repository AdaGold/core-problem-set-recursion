# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError("Can't use negative numbers")

    if n == 1:
        return 1

    return n * factorial(n - 1)


# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    if count == 0:
        return 0

    return 2 + bunny(count - 1)


# is_nested_parens
def is_nested_parens(parens):
    # need to count open
    def count_parens(parens, chart_to_count):
        # parens, ")"
        # if open != closed
        pass
    pass


def is_nested_parens(parens):
    def proper_count(string, open_count, close_count):
        pass
    pass

