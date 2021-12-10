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
    if not text:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(a, b):
    match = 0
    recurse = 0

    if a % 10 == b % 10:
        match = 1

    new_a = a//10
    new_b = b//10

    if new_a != 0 and new_b != 0:
        recurse = digit_match(new_a, new_b)
    
    return match + recurse

