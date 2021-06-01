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
    if len(text) <= 1:
        return True
    elif text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    return False


# digit_match
def digit_match(apples, oranges):
    apples = str(apples)
    oranges = str(oranges)
    if len(apples) <= 1 or len(oranges) <= 1:
        if apples[-1] == oranges[-1]:
            return 1
        return 0
    if len(apples) >= 2 and len(oranges) >= 2:
        if apples[-1] == oranges[-1]:
            return 1 + digit_match(apples[:-1], oranges[:-1])
        return digit_match(apples[:-1], oranges[:-1])

