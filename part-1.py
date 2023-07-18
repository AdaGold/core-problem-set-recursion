# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# reverse

def reverse(text):
    return text[::-1]

# bunny

def bunny(count):
    if count == 0:
        return 0
    else:
        return 2 + bunny(count - 1)



# is_nested_parens

def is_nested_parens(parens):
    stack = []

    for char in parens:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0 or stack.pop() != "(":
                return False

    return len(stack) == 0

