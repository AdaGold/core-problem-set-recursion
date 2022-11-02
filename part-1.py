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

    return n * factorial(n-1)


# reverse
def reverse(text):
    if text == "":
        return ""

    letter = text[len(text) - 1]
    text = text[:-1]

    return letter + reverse(text)


# bunny
def bunny(count):
    if count == 0:
        return 0

    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True

    open_paren_index = int(len(parens)/2 - 1)

    if parens[open_paren_index:open_paren_index + 2] != '()':
        return False

    parens = parens.replace('()', '')
    return True and is_nested_parens(parens)
