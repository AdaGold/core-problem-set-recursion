# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num == 0:
        return 1
    elif num < 0:
        raise ValueError
    
    return num * factorial(num - 1)


# reverse
def reverse(text):
    if text == '':
        return text
    length = len(text)
    return text[length-1:length] + reverse(text[:-1])


# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count-1)
        


# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    
    if parens[:1] != '(' or parens[-1] != ")":
        return False
    return  is_nested_parens(parens[1:-1])
