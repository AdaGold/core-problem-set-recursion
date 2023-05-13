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

    if len(text) < 1:
        return True
    else:
        if text[0] != text[-1]:
            return False
        else:
            return is_palindrome(text[1:-1])


# digit_match
# this solution does not work
def digit_match(num1, num2):
    tot = 0
    if len(num1) == 0 or len(num2) == 0:
        return tot
    elif num1[-1] == num2[-1]:
        tot += 1
    return digit_match(num1[:-1], num2[:-1])

