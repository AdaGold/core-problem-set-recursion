# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(int_list, query_item):
    if not int_list:
        return False

    return int_list[0] == query_item or search(int_list[1:], query_item)


# is_palindrome

def is_palindrome(text):
    if not text:
        return True

    return text[0] == text[-1] and is_palindrome(text[1:-1])

# digit_match

def is_palindrome(text):
    if not text:
        return True

    return text[0] == text[-1] and is_palindrome(text[1:-1])