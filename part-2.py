# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    if array[0] == query:
        return True
    else:
        return search(array[1:], query)

# is_palindrome
def is_palindrome(text):
    if not text:
        return True
    
    return text[0]==text[-1] and is_palindrome(text[1:-1])


# digit_match
def digit_match(num1, num2):
    
    # if any of two input numbers has only one digit, check last digit
    if num1//10 == 0 or num2//10 == 0:
        if num1%10 == num2%10:
            return 1
        return 0
        
    count = 0
    if num1%10 == num2%10:
        count += 1
    
    return count + digit_match(num1//10, num2//10)

