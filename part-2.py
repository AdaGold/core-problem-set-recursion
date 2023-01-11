# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array,query):
    if not array:
        return False

    if array[0] == query:
        return True
    else:
        return search(array[1:],query)


# is_palindrome
def is_palindrome(text):
    if not text:
        return True

    text_len = len(text)
    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


# digit_match
def digit_match(number1, number2):
    if number1 == number2:
        return 1

    if number1 == 0 or number2 == 0:
        return 0
    
    next_number1 = number1 // 10
    next_number2 = number2 // 10
    
    if (number1 % 10) == (number2 % 10):
        return 1 + digit_match(next_number1,next_number2)
    
    if next_number1 == 0 and next_number2 == 0:
        return 0
    
    return digit_match(next_number1,next_number2)

