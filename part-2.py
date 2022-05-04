# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    
    if len(array) == 0:
        return False
    if array[0] == query:
        return True
        
    return search(array[1:], query)


# is_palindrome
# Solution 1:
def is_palindrome(text):
    if len(text) <= 1:
        return True
    
    return is_palindrome(text[1:-1]) and text[0] == text[-1]
    
# Solution 2:
def is_palindrome(text):
    if len(text) <= 1:
        return True
    
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    else:
        return False


# digit_match
def digit_match(num1, num2):
    
    count = 0
    digit1 = num1 % 10
    digit2 = num2 % 10
    
    if digit1 == digit2:
        count += 1
        
    if num1 < 10 or num2 < 10:
        return count
    
    return count + digit_match(num1//10, num2//10)

