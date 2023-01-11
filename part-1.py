# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num < 0:
        raise ValueError("Num must be greater than zero")
    if num == 0:
        return 1
    else:
       return num * factorial(num-1)


# reverse
def reverse(text):
    if not text:
        return ""

    str_len= len(text)
    if  str_len == 1:
        return text
    else:
        return text[-1] + reverse(text[:-1])


# bunny
def bunny(num):
    if not num:
        return 0

    if num == 1:
        return 2
    
    return 2 + bunny(num-1)


# is_nested_parens
def is_nested_parens(parentesis):
    if not parentesis:
        return True

    str_len = len(parentesis)

    if parentesis[0]=='('and parentesis[-1]!=')':
        return False
    if parentesis[0]==')':
        return False

    return is_nested_parens(parentesis[1:-1])


