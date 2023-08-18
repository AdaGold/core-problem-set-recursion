# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def is_nested_parens(parens):
    if not parens:
        return True
    if len(parens) == 1:
        return False
    if len(parens) == 2:
        if parens[0] == ")" and parens[1] == "(":
            return False
        if parens[0] == parens[1]:
            return False
        
    return is_nested_parens(parens[1:-1])


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    return False


# digit_match
def digit_match(x,y):
    x=str(x)
    y=str(y)
    count=0
    if len(x) == 0 or len(y) == 0:
        return count
    if x[-1] == y[-1]:
        count += 1
        count += digit_match(x[:-1], y[:-1])
    elif x[-1] != y[-1]:
        count += digit_match(x[:-1], y[:-1])
    return count

