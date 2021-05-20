# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    # Base case 
    while n >= 0:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    raise ValueError


# reverse
def reverse(text):
    if len(text) == 0:
        return text
    else:
        return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    if (count == 0):
        return 0
    else:
        return 2 + bunny (count - 1)


# is_nested_parens
def is_nested_parens(parens):
    stack = []
    for paren in parens:
        if paren == '(':
            stack.append(paren)
        else:
            if not stack:
                return False
    else:
        top = stack[-1]
        if paren == ')' and top == '(':
            stack.pop()
        if not stack:
            return True 
        else:
            return False

