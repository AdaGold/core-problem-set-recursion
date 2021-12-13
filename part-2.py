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
    else:
        return search(array[1:], query)



# is_palindrome
def is_palindrome(text):
    if not text:
        return True 
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    else:
        return False



# digit_match
def digit_match(apples, oranges):
    if apples == 0 and oranges != 0:
        return 0
    elif apples != 0 and oranges == 0:
        return 0
    elif apples == 0 and oranges == 0:
        return 1
    elif apples % 10 == oranges % 10:
        return 1 + digit_match(apples // 10, oranges // 10)
    elif apples % 10 != oranges % 10:
        if 1 <= apples < 10 and 1 <= oranges < 10:
            return 0
        return digit_match(apples // 10, oranges // 10)


