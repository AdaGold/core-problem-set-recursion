# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(number):
    if number < 0:
        raise ValueError("Negative Number factorial can not be found")
    if number == 0:
        return 1
    if number == 1:
        return 1
    return number * factorial(number-1)
    


# reverse
def reverse(str):
    if len(str) == 0:
        return ""
    if len(str) == 1:
        return str
    length = len(str)
        
    return str[-1] + reverse(str[0:length-1])


# bunny
def bunny(count):
    if count == 0:
        return 0
    if count == 1:
        return 2
    return 2 + bunny(count-1)


# is_nested_parens

def is_nested_parens(str):
    if str == "":
        return True
    length = len(str)
    if str[0] == "(" and str[length-1] == ")":
        return is_nested_parens(str[1:length-1])
    else:
        return False
