# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n == 0:
        return 1
    
    elif n > 0:
        return n * factorial(n-1)
    
    else:
        raise ValueError

# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    else:
        return text[::-1]

# bunny
"""
I had a hard time coming up with a correct base case,
but eventually understood how to use recursion for this
problem. It's the same as the provided solution, but I broke
it down line by line to understand the logic!
"""
def bunny(count):
    if not count:
        return count
    else: 
        return 2 + bunny(count-1)


# is_nested_parens
"""
I worked through the solution with recursion on my
own, but just needed to understand the logic first-
hence no recursion haha.
"""
# my original solution (not using recursion)
def is_nested_parens(parens):
    count = 0
    if len(parens) == 0:
        return True
    else:
        for paren in parens:
            if paren == ')':
                if count <= 0:
                    return False
                count -= 1
            elif paren == "(":
                count += 1
        return True

# correct solution
def is_nested_parens(parens):
    count = 0
    if len(parens) == 0:
        return True
    elif parens[:1] != "(" or parens[-1:] != ")":
        return False
    else:
        return is_nested_parens(parens[1:-1])


