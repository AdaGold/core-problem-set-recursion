# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search (array, query):
    if query not in array:
        return False
    elif query in array:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) == 0:
        return True
    elif text[0] != text[-1:]:
        return False
    else:
        return is_palindrome(text[1:-1]) 


# digit_match


