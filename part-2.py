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
    # Use Python slicing to get all items
    # besides the first item
    return search(array[1:], query)

# is_palindrome
def is_palindrome(text:str) -> bool:
    if text == "" or len(text) == 1: 
        return True
    
    return text[0] == text[-1] and is_palindrome(text[1:-1])

# digit_match
def digit_match(apples, oranges):
    digit_from_apple = apples % 10
    digit_from_oranges = oranges % 10
    
    count = 0
    if digit_from_apple == digit_from_oranges:
        count += 1
    if apples < 10 or oranges < 10:
        return count
    return count + digit_match(apples // 10, oranges // 10)

