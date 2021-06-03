# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if query not in array:
        return False
    else: 
        return True


# is_palindrome
def is_palindrome(string):
    return string == string[::-1]


# digit_match
def digit_match(apples, oranges):
    if apples == 0 and oranges == 0:
        return 1
    elif apples < 10 or oranges < 10:
        if apples % 10 == oranges % 10:
            return 1
        return 0
    if apples % 10 == oranges % 10:
        return 1 + digit_match(apples // 10, oranges // 10)
    return digit_match(apples // 10, oranges // 10)

