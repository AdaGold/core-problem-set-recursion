# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) <= 0:
        return False
    elif str(array[0]) == query:
        return True
    elif str(array[0]) != query:
        the_rest = str(array[1:])
        return search(the_rest, query)
    else:
        return False


# is_palindrome
def is_palindrome(text):
    size = len(text)
    if size <= 1:
        return True
    elif str(text[0]) == str(text[-1]):
        inside = str(text[1:-1])
        return is_palindrome(inside)
    else:
        return False


# digit_match
def digit_match(num1, num2):
    if num1 < 10 and num2 < 10:
        if num1 == num2:
            return 1
        elif num1 != num2:
            return 0
    if num1 == 0 or num2 == 0:
        return 0
    units1 = num1 % 10
    units2 = num2 % 10
    if units1 == units2:
        return  1 + digit_match(num1 // 10, num2 // 10)
    else:
        return digit_match(num1 // 10, num2 // 10)

