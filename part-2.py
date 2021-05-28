# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, q):
    if len(array) == 0:
        return False
    if array[0] == q:
        return True
    return search(array[1:], q)


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])



# digit_match
def digit_match(x, y, count =0):
    x = str(x)
    y = str(y)
    if len(x) == 0 or len(y) == 0:
        return count
    if x[-1] == y[-1]:
        return digit_match(x[:-1], y[:-1], count+1)
    elif x[0] != y[0]:
        return digit_match(x[:-1], y[:-1], count)
    

