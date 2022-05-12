# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    # base cases
    if not array:
        return False

    if array[0] == query:
        return True

    if len(array) == 1 and array[0] != query:
        return False

    # recursive case - search rest of array
    return search(array[1:], query)

# is_palindrome
def is_palindrome(text):
    if len(text) <= 2:
        if len(text) == 2:
            if text[0] != text[1]:
                return False
            else:
                return True
        if len(text) == 1:
            return True
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(string1, string2):
    string1 = str(string1)
    string2 = str(string2)
    matches = 0
    
    if not string1 or not string2:
        return matches
    
    if string1[-1] == string2[-1]:
        matches = 1

    return digit_match(string1[:-1], string2[:-1]) + matches

