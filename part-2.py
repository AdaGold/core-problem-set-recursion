# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
    elif array[0] == query:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    elif text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(x, y):
    if x < 10 or y < 10:
        if x % 10 == y % 10:
            return 1
        else:
            return 0
    elif x % 10 == y % 10:  
        return 1 + digit_match(x//10, y//10)
    else:
        return digit_match(x//10, y//10)

