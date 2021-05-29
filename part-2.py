# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
       return False
    if len(array) == 1 and array[0] != query:
        return False
    if array[0] == query:
        return True
    return search(array[1:],query)

# is_palindrome
def is_palindrome(text):
    if len(text) == 1 or not text:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])

# digit_match
def digit_match(apples, oranges, count = 0):
    if apples == 0 and oranges == 0:
        return 1
    if apples < 10 or oranges < 10:
        if apples % 10 == oranges % 10:
            count += 1
        return count
    if apples % 10 == oranges % 10:
        count += 1
    return digit_match(apples//10, oranges//10, count) 

