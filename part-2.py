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
    def helper(left, right):
        if right - left <= 0:
            return True
        elif text[left] != text[right]:
            return False
        else:
            return helper(left + 1, right - 1)
    
    return helper(0, len(text) - 1)


# digit_match
def digit_match(left, right, matches=0):
    if left == 0 and right == 0:
        return matches + 1
    elif left < 10 or right < 10:
        if left % 10 == right % 10:
            return matches + 1
        else:
            return matches
    elif left % 10 == right % 10:
        return digit_match(left // 10, right // 10, matches + 1)
    else:
        return digit_match(left // 10, right // 10, matches)

