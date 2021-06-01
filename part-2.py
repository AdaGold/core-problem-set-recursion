# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not len(array):
        return False
    elif array[0] == query:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    return text == text[::-1]


# digit_match
def digit_match(apples, oranges):
    # Base cases:
    # If both apples and oranges are 0 return 1
    if apples == 0 and oranges == 0:
        return 1
    # If one or both are 1-digit numbers
    elif apples < 10 or oranges < 10:
        if apples % 10 == oranges % 10:
            return 1
        return 0
    # Recursive Cases
    # Continues to repeat as it works through each digit from the end
    # And once base case is met, the call stack is returned
    if apples % 10 == oranges % 10:
        return 1 + digit_match(apples // 10, oranges // 10)
    return digit_match(apples // 10, oranges // 10)

