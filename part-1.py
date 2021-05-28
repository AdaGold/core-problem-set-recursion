# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    if n <= 1: 
        return 1

    return n * factorial(n - 1)


# reverse
def reverse(string):

    if len(string) <= 0:
        return string
    else:
        return reverse(string[1:]) + string[0]


# bunny
def bunny(count):
    if count == 0:
        return count
  
    return 2 + bunny(count - 1)


# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True

    if len(parens) == 2 and parens[0] != parens[-1]:
        return True
  
    if len(parens) == 1 or parens[0] == parens[-1]:
        return False
    
    return is_nested_parens(parens[1:-1])

