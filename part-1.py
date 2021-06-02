# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    elif  n < 2:
        return 1
    else:
        return n * factorial(n-1)


# reverse

def reverse(text):
    if len(text)==1 or len(text)== 0:
        return text     
    else:
        return text[-1] + reverse(text[:-1])

# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count - 1)



# is_nested_parens
def is_nested_parens(parens):
    left_parenthesis = []
    right_parenthesis = []
    for char in parens:
        if char == "(":
            left_parenthesis.append(char)
        elif char == ")":
            right_parenthesis.append(char)
    if len(left_parenthesis) == len(right_parenthesis):
        return True
    return False


