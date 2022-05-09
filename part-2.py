# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
    if array[len(array)-1] == query:
        return True

    return search(array[:-1], query)


# is_palindrome
def is_palindrome(text):
    if len(text) < 2:
        return True
    if text[0] != text[-1]:
        return False
    else:
        return is_palindrome(text[1:-1])


# digit_match
def digit_match(apples, oranges):
    apples = str(apples)
    oranges = str(oranges)
    return helper(apples, oranges,  len(apples) - 1, len(oranges) - 1, 0)

def helper(apples, oranges, idx_app, idx_or, counter):
    if idx_app < 0 or idx_or < 0:
        return counter
    if apples[idx_app] == oranges[idx_or]:
        counter += 1
    return helper(apples, oranges, idx_app - 1, idx_or - 1, counter)

