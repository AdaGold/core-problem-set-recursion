# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n<0:
        raise ValueError("No negative Numbers accepted")
    
    if n == 1 or n == 0:
        return 1
        
    return n * factorial(n-1)


# reverse
def reverse(word):
    if len(word) == 0:
        return ""
    return word[-1] + reverse(word[0:-1])


# bunny
def bunny(count):
    if count == 0:
        return count
    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(str):
    if str == "":
        return True
    elif str[0] == "(" and str[-1] == ")":
        return is_nested_parens(str[1: -1])
    else:
        return False


