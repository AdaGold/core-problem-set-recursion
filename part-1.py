# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n <0:
        raise ValueError
    
    if n == 0:
        return 1
    
    return n * factorial(n-1)
        


# reverse
def reverse(text):
    n = len(text)
    if n == 0:
        return text
    return reverse(text[1:])+text[0]


# bunny
def bunny(count):
    if count == 0:
        return count
    return 2+bunny(count-1)

# is_nested_parens


