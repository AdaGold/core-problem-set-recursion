# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n<0:
        raise ValueError
    if n == 0:
        return 1
    return n*factorial(n-1)

# reverse
def reverse(string):
    if len(string)<=1:
        return string
    first = string[0]
    other = string[1:]
    return reverse(other)+first

# bunny
def bunny(num):
    if num == 0:
        return 0
    return 2+bunny(num-1)

# is_nested_parens

def is_nested_parens(string):
    print(string)
    if string == "":
        return True
    if string =="((" or string=="))":
        return False
    if string[0]+string[-1]=="()":
        return is_nested_parens(string[1:-1])
