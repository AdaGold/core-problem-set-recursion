# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array, query):
    for item in array:
        if isinstance(item, list):
            return search(array, query)
        if query in array:
            return True
    else:
        return False

# is_palindrome

def is_palindrome(text):
    
    if len(text) <= 1:
        return True
        
    elif text[0] != text[-1]:
        return False
        
    else:
        return is_palindrome(text[1:-1])

# digit_match

def digit_match(num1, num2):
    count = 0 

    num1 = str(num1)
    num2 = str(num2)

    if len(num1) == 0 or len(num2) == 0:
        return count

    if int(num1[-1]) == int(num2[-1]):
        count += 1

    if len(num1) != 0 and len(num2) != 0:
        count += digit_match(num1[0:-1], num2[0:-1]) 
        return count

