# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    elif array[0] == query:
        return True
    
    return search(array[1:], query) 


# is_palindrome
def is_palindrome(text):
    if len(text) == 3 or len(text) == 2:
        return text[0] == text[-1]

    return is_palindrome(text[1:-1])


# digit_match
def digit_match(num_1, num_2):
    # Base case: we're at the beginning of the num
    if num_1 < 10 or num_2 < 10:
        if num_1 % 10 == num_2 % 10:
            return 1
        else:
            return 0

    # Recursive case
    if num_1 % 10 == num_2 % 10: 
        return 1 + digit_match(num_1 // 10, num_2 // 10)
    else:
        return digit_match(num_1 // 10, num_2 // 10)



