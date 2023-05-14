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
    if text == "":
        return True
    
    if len(text) == 1:
        return True
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    else:
        return False


# digit_match
def digit_match(n1, n2):
    n1 = str(n1)    
    n2 = str(n2)

    if n1 == "" or n2 == "":
        return 0

    if n1[-1] == n2[-1]:
        return 1 + digit_match(n1[:-1], n2[:-1])
    return 0 + digit_match(n1[:-1], n2[:-1])

