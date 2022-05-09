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
    else:
        return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) == 1:
        return True
    elif text[0] != text[-1:]:
        return False
    else:
        return is_palindrome(text[1:-1])



# digit_match
def digit_match(first, second):
    if first == 0 and second == 0:
        return 1
    if first < 10 or second < 10:
        if first % 10 == second % 10:
            return 1
        else:
            return 0
    elif first % 10 == second % 10:
        return 1 + digit_match((first // 10), (second // 10))
    else:
        return digit_match((first // 10), (second // 10))

