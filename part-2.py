# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not len(array):
        return False
    if array[0] == query:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) == 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
# i felt pretty good about the other problems
# but felt COMPLETELY lost with this one
# i'm still not sure why or how i got it to work
# and i'm sure i have unnecessary things here
def digit_match(a,b):
    if a == b:
        return 1

    a_digit = a % 10
    b_digit = b % 10


    a_next = a // 10
    b_next = b // 10


    if a_digit == b_digit:
        if a < 10 or b < 10:
            return 1
        return 1 + digit_match(a_next, b_next)
    elif a >= 10 and b >= 10:
        return digit_match(a_next, b_next)
    return 0

