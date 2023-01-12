# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    elif n == 0:
        return 1
    elif n == 1:
        return n
    return n * factorial(n-1)


# reverse
def reverse(string):
    if len(string) == 1:
        return string
    elif len(string) == 0:
        return ""
    
    temp = string[0]
    return reverse(string[1:]) + temp


# bunny
def bunny(count):
    if count == 0:
        return 0
    elif count == 1:
        return 2
        
    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens):
    
    if parens == "":
        return True
    elif len(parens)%2 != 0:
        return False
    elif parens[0] =="(" and parens[len(parens)-1] ==")":
        return True and is_nested_parens(parens[1:len(parens)-1])

