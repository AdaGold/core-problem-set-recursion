# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    elif array[0] == query:
        return True
    else:
        return search(array[1:],query)


# is_palindrome

def is_palindrome(text):
    if len(text) <= 1:
        return True
    elif text[0] == text[-1]:# if the first and last are same
        return is_palindrome(text[1:-1]) # continue calling self to check for the next
    else:
        return False # otherwise return False

# digit_match

def digit_match(apples, oranges):
    if apples == 0 and oranges == 0:
        return 1
    elif apples < 10 or oranges < 10:
        return int(apples % 10 == oranges % 10)
    elif apples % 10 == oranges % 10:
        return 1 + digit_match(apples // 10, oranges // 10)
    else:
        return digit_match(apples // 10, oranges // 10)
