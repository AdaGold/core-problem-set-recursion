# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if array == []:
        return False
    if array[0] == query:
        return True
    array.remove(array[0])
    return search(array, query)

# is_palindrome
def is_palindrome(text):
    if len(text) == 1:
        return True
    if text[0] != text [-1]:
        return False
    return is_palindrome(text[1:-1])

# digit_match
def digit_match(num1, num2):
    if num1 == 0 and num2 == 0:
        return 1
    
    elif num1 < 10 or num2 < 10:
        if num1 % 10 == num2 % 10:
            return 1
        return 0
    
    if num1 % 10 == num2 % 10:
        return 1 + digit_match(num1//10, num2//10)
    
    return digit_match(num1//10, num2//10)

