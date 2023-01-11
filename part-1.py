# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n, acc=1):
    #base case
    if n < 0:
        raise ValueError
    if n <= 1:
        return acc
    
    return factorial(n-1, n*acc)



# reverse
def reverse(text, acc=""):
    if len(text) <= 0:
        return acc
    return reverse(text[:-1], acc + text[-1])



# bunny
def bunny(count, acc=0):
    if count == 0:
        return acc
        
    return bunny(count-1, acc + 2)


# is_nested_parens
def is_nested_parens(parens, index=0, depth=0):
    if index == len(parens):
        return depth == 0
    if depth < 0:
        return False
    
    if parens[index] == "(":
        return is_nested_parens(parens, index + 1, depth + 1)
    elif parens[index] == ")":
        return is_nested_parens(parens, index + 1, depth - 1)
    else:
        return False


