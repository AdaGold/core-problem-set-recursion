# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if array == []:
        return False

    return query == array[0] or search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) < 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(apples, oranges):
    #checks if inputs are both 0
    if apples == oranges:
        return 1
    #checks if either inputs are one digit nums
    if apples < 10 or oranges < 10:
        if apples % 10 == oranges % 10:
            return 1
        return 0
    one = apples // 10
    two = oranges // 10
    
    if apples % 10 == oranges % 10:
        return digit_match(one, two) + 1
    return digit_match(one, two)

