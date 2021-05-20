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
    if len(text) == 0:
        return True
    elif text[0] != text[-1]:
        return False
        
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(num_1, num_2):
    if len(str(num_1)) == 0 or len(str(num_2)) == 0:
        return 0
    elif str(num_1)[-1] == str(num_2)[-1]:
        return digit_match(str(num_1)[:-1], str(num_2)[:-1]) + 1
        
    return digit_match(str(num_1)[:-1], str(num_2)[:-1])

