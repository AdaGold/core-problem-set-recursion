# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    try:
        n >= 0
    except:
        raise ValueError
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)


# reverse
def reverse(text):
    if text == "":
        return text
    return text[-1] + reverse(text[:-1])


# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count-1)


# is_nested_parens
stack = list()

def is_nested_parens(parens):
    if not parens:
        if not stack:
            return True
        return False

    if parens[0] == '(':
        stack.append(parens[0])
    elif parens[0] == ')':
        if stack:
            stack.pop()
        else:
            return False
    return is_nested_parens(parens[1:])

