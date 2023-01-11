# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    if query == array[0]:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if not text:
        return True
    l = text[0]
    r = text[-1]
    if l != r:
        return False
    else:
        return is_palindrome(text[1:-1])


# digit_match
def digit_match(num1, num2):
    if num1 < 10 or num2 < 10:
        if (num1 % 10) == (num2 % 10):
            return 1
        else:
            return 0
            
    else:
        if (num1 % 10) == (num2 % 10):
            return 1 + digit_match((num1 // 10), (num2 // 10))
        else:
            return 0 + digit_match((num1 // 10), (num2 // 10))