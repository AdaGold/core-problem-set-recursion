# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(unsorted_array, query):
    if len(unsorted_array) == 0:
        return False
    first_item = unsorted_array[0]
    if first_item == query:
        return True
    return search(unsorted_array[1:], query)

# is_palindrome

def is_palindrome(text):
    if len(text) <= 1:
        return True
    elif text[:1] != text[-1:]:
        return False
    else:
        return is_palindrome(text[1:-1])

# digit_match

def digit_match(int_one, int_two):
    next_int_one = int_one//10
    next_int_two = int_two//10
    match_score = int((int_one % 10) == (int_two % 10))

    if (next_int_one == 0) or (next_int_two == 0):
        return match_score
    else:
        return match_score + digit_match(next_int_one, next_int_two)
