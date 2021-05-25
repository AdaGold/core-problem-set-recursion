# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
    if array[-1] == query:
        return True
    return search(array[:-1], query)


# is_palindrome
def is_palindrome(text):
    if len(text) == 1 or not text:
        return True
    elif text[0] != text[-1]:
        return False
    else:
        return is_palindrome(text[1:-1])


# digit_match
import math
def digit_match(x, y):
    if x == 0 and y == 0:
        return 1
    if x == 0:
        if y % 10 == 0:
            return 1
        else:
            return 0
    if y == 0:
        if x % 10 == 0:
            return 1
        else:
            return 0
    if math.floor(x) == 0 or math.floor(y) == 0:
        return 0
    match = 1 if math.floor(x) % 10 == math.floor(y) % 10 else 0
    return digit_match(x/10, y/10) + match

