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

    if len(text) == 1 or len(text) == 0:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])

# digit_match
def digit_match(int1, int2):

    if int1 == 0 and int2 == 0:
        return 1

    match_count = 0

    if int1 % 10 == int2 % 10:
        match_count += 1

    if int1//10 == 0 or int2//10 == 0:
        return match_count
    return match_count + digit_match(int1//10, int2//10)
