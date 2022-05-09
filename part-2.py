# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    # base case 
    if len(array) == 0:
        return False
    if array[0] == query:
        return True
    # recursive case
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    # base case
    if len(text) == 1:
        return True
    # recursive case
    elif text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    return False


# digit_match
def digit_match(int_a, int_b):
    # base case
    if int_a == 0 and int_b == 0:
        return 1
    elif int_a < 10 or int_b < 10: 
        if int_a % 10 == int_b % 10:
            return 1
        else:
            return 0
    # recursive case
    if int_a % 10 == int_b % 10: 
        return digit_match(int_a // 10, int_b // 10) + 1 
    else:
        return digit_match(int_a // 10, int_b // 10)

