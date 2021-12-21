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
            return helper(left + 1, right -1)
           
    return helper(0, len(text) - 1)


# digit_match
def digit_match(int1, int2, matches=0):
    if int1 == 0 and int2 == 0:
        return matches + 1
    elif int1 < 10 or int2 < 10:
        if int1 % 10 == int2 % 10:
            return matches + 1
        else:
            return matches
    elif int1 % 10 == int2 % 10:
        return digit_match(int1 // 10, int2 // 10, matches + 1)
    else:
        return digit_match(int1 // 10, int2 // 10, matches)

