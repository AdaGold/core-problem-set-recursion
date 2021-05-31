# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(in_array, query):
    if len(in_array) <= 0:
        return False
    elif in_array[0] == query:
        return True
    new_array = in_array[1:]
    return search(new_array, query)


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    elif text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    else:
        return False


# digit_match
def digit_match(apples, oranges):
    if apples <= 1 or oranges <= 1:
        if apples != oranges:
            return 0
        else: 
            return 1
    else:
        matching_pairs = apples % 10 == oranges % 10
        return matching_pairs + digit_match(apples//10, oranges//10)

