# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
        
    return (array[0] == query or search(array[1:], query))


# is_palindrome
def is_palindrome(text):
    if len(text) < 2:
        return True
    
    elif text[0] == text[-1]:
        return is_palindrome(text[1:-1])
        
    return False


# digit_match
def digit_match(num1, num2):
    digit1 = num1 % 10
    digit2 = num2 % 10
    
    if (digit1 == digit2):
        count = 1
    else:
        count = 0
        
    if num1 // 10 == 0 or num2 // 10 == 0:
        return count
        
    return count + digit_match(num1//10, num2//10)

