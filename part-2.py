# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array, query, i=0):
    if len(array) == i:
        return False
    elif array[i] == query:
        return True
    else:
        return search(array, query, i + 1)


# is_palindrome

def is_palindrome(text):
    if len(text) == 1:
        return True
    elif text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    return False


# digit_match

def digit_match(left, right, matches=0):
    if left == 0 and right == 0:
        return matches + 1

    if left < 10 or right < 10:
        if left % 10 == right % 10:
            return matches + 1
        else:
            return matches

    elif left % 10 == right % 10:
        return digit_match(left//10, right//10, matches + 1)

    else:
        return digit_match(left//10, right//10, matches)
