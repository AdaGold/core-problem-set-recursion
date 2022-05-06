# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
    if array[0] == query:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[-1] != text[0]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(int_a, int_b):
    a = str(int_a)
    b = str(int_b)
    if len(a) == 0 or len(b) == 0:
        return 0
    if a[-1] == b[-1]:
        return 1 + digit_match(a[:-1], b[:-1])
    else:
        return 0 + digit_match(a[:-1], b[:-1])
        

