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
        elif text[left] == text[right]:
            return helper(left + 1, right - 1)
        return False

    return helper(0, len(text) - 1)


# digit_match


def digit_match(num1, num2):
    if num1 == 0 and num2 == 0:
        return 1

    elif num1 < 10 or num2 < 10:
        if num1 % 10 == num2 % 10:
            return 1
        return 0

    if num1 % 10 == num2 % 10:
        return 1 + digit_match(num1 // 10, num2 // 10)
    return digit_match(num1 // 10, num2 // 10)
