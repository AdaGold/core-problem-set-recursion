# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array, query):
    if not array:
        return False
    if array[0] == query:
        return True
    return search(array[1:], query)

# is_palindrome

def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])

# digit_match

def digit_match(n1, n2):
    if n1 // 10 <= 0 or n2 // 10 <= 0:
        return 1 if n1 % 10 == n2 % 10 else 0
    if n1 % 10 == n2 % 10:
        return 1 + digit_match(n1 // 10, n2 // 10)
    return digit_match(n1 // 10, n2 // 10)
